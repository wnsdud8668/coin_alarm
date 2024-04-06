import pyupbit
import time
import requests
import time
import numpy as np


def post_message(token, channel, text):
    response = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer " + token},
        data={"channel": channel, "text": text},
    )
    print(response)


def tickers_db(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="day", count=210)
    return df


myToken = "xoxb-4019297737527-4036330620788-OuSqeGVPvGEomCxlGlvHyoIh"

try:
    coin_nm_lst = [
        "BTC",
        "XRP",
        "ETH",
        "NEO",
        "MANA",
        "SAND",
        "BORA",
        "ONG",
        "DOGE",
        "SOL",
        "QTUM",
        "JST",
        "AXS",
        "MATIC",
        "FLOW",
        # "NU",
        "ONT",
        "ADA",
        "ATOM",
        "NEAR",
        "KNC",
        "ETC",
        "POWR",
        "AVAX",
        "WAVES",
        "EOS",
        "CVC",
        "REP",
        "TRX",
        "SXP",
        "VET",
        "TFUEL",
        "STX",
        "PLA",
        "CRO",
        "LINK",
        "HUNT",
        "PUNDIX",
        "GAS",
        "1INCH",
        "DOT",
        "THETA",
        "ENJ",
        "XLM",
        "CRE",
        "SRM",
        "ALGO",
        "SC",
        "ICX",
        #'BTT',
        "CHZ",
        "META",
        "BAT",
        "KAVA",
        "XEC",
        "LOOM",
        "XTZ",
        "WAXP",
        "AAVE",
        "HUM",
        "HBAR",
        "STRK",
        "HIVE",
        "STPT",
        "STORJ",
        "OMG",
        "FCT2",
        "MOC",
        "MLK",
        "DAWN",
        "TT",
        "MED",
        "QKC",
        "BCH",
        "ZIL",
        "SBD",
        "XEM",
        "AQT",
        "ANKR",
        "ZRX",
        "LSK",
        "BTG",
        "STRAX",
        "MTL",
        "ELF",
        "IOTA",
        "CBK",
        #'MFT',
        "STMX",
        "IQ",
        "TON",
        "UPP",
        "SNT",
        "AERGO",
        "GLM",
        "DKA",
        "SSX",
        "MVL",
        "ORBS",
        "ARK",
        "RFR",
        "ARDR",
        "IOST",
        "MBL",
        "STEEM",
        "BSV",
        "GRS",
        "AHT",
    ]

    # coin_nm_lst=['ATOM']

    coin_lst = []

    for coin_nm in coin_nm_lst:
        time.sleep(0.1)
        df = tickers_db("KRW-{}".format(coin_nm))[
            ["high", "low", "open", "close", "volume"]
        ]

        ma_30 = np.mean(df["close"])

        yesterday_price = tickers_db("KRW-{}".format(coin_nm))["close"].iloc[-2]

        now_price = tickers_db("KRW-{}".format(coin_nm))["close"].iloc[-1]

        vol_avg_4week = np.mean(df["volume"].iloc[-29:-1])

        now_vol = tickers_db("KRW-{}".format(coin_nm))["volume"].iloc[-1]

        if (
            (now_price > ma_30)
            & (yesterday_price < ma_30)
            & (vol_avg_4week * 1.9 < now_vol)
        ):
            coin_lst.append(coin_nm)
        time.sleep(0.1)

except Exception as e:
    print(coin_nm)
    print(e)

post_message(myToken, "#코인알라미", "코인리스트 : " + str(coin_lst))
