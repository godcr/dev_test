import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas_datareader.data as web
import pandas as pd
from pandas import Series, DataFrame
from datetime import datetime

from matplotlib import font_manager, rc

rc('font', family='AppleGothic')

plt.rcParams['axes.unicode_minus'] = False


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(600, 200, 1200, 600)
        self.setWindowTitle("PyChart Viewer v0.1")
        self.setWindowIcon(QIcon('icon.png'))

        self.lineEdit = QLineEdit()
        self.pushButton = QPushButton("차트그리기")
        self.pushButton.clicked.connect(self.pushButtonClicked)

        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)

        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.canvas)

        # Right Layout
        rightLayout = QVBoxLayout()
        rightLayout.addWidget(self.lineEdit)
        rightLayout.addWidget(self.pushButton)
        rightLayout.addStretch(1)

        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)
        layout.setStretchFactor(leftLayout, 1)
        layout.setStretchFactor(rightLayout, 0)

        self.setLayout(layout)

    def pushButtonClicked(self):
        code = self.lineEdit.text()

        ax = self.fig.add_subplot(211)
        ax.plot([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0])
        ax.set_xlabel('x축')
        ax.set_ylabel('y축')
        ax.grid()

        ax = self.fig.add_subplot(212)
        ax.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        ax.grid()

        # self.getGoogleData(ax)


        self.canvas.draw()

        # df = web.DataReader(code, "yahoo")
        # df['MA20'] = df['Adj Close'].rolling(window=20).mean()
        # df['MA60'] = df['Adj Close'].rolling(window=60).mean()

        # df = []
        # df['MA20'] = [20, 30, 40]
        # df['MA60'] = [15, 25, 35]
        #
        # ax = self.fig.add_subplot(111)
        # # ax.plot(df.index, df['Adj Close'], label='Adj Close')
        # ax.plot(df.index, df['MA20'], label='MA20')
        # ax.plot(df.index, df['MA60'], label='MA60')
        # ax.legend(loc='upper right')
        # ax.grid()
        #
        # self.canvas.draw()


    def getGoogleData(self, ax):
        start = datetime(2015, 1, 1)
        end = datetime.now()
        KA = web.DataReader('KRX:003490', 'google', start, end)

        KA.head(10)
        KA['Close'].plot(style='--')
        pd.rolling_mean(KA['Close'], 7).plot(lw=2)
        ax.set_legend(['종가시세', '이동평균선 7일'])



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()