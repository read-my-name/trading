{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyNe8m2XCP8nq2yxrMdQSxyO"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","source":["!pip install yfinance\n","!pip show yfinance"],"metadata":{"id":"2OqEYxM1M7Yv","colab":{"base_uri":"https://localhost:8080/"},"executionInfo":{"status":"ok","timestamp":1679926901883,"user_tz":-480,"elapsed":16347,"user":{"displayName":"Tan Jun Xuan","userId":"00319716665018572021"}},"outputId":"3b136f05-c4b9-4d99-a0ec-fe72ec6eba0a"},"execution_count":1,"outputs":[{"output_type":"stream","name":"stdout","text":["Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n","Requirement already satisfied: yfinance in /usr/local/lib/python3.9/dist-packages (0.2.13)\n","Requirement already satisfied: beautifulsoup4>=4.11.1 in /usr/local/lib/python3.9/dist-packages (from yfinance) (4.11.2)\n","Requirement already satisfied: html5lib>=1.1 in /usr/local/lib/python3.9/dist-packages (from yfinance) (1.1)\n","Requirement already satisfied: pytz>=2022.5 in /usr/local/lib/python3.9/dist-packages (from yfinance) (2022.7.1)\n","Requirement already satisfied: frozendict>=2.3.4 in /usr/local/lib/python3.9/dist-packages (from yfinance) (2.3.6)\n","Requirement already satisfied: multitasking>=0.0.7 in /usr/local/lib/python3.9/dist-packages (from yfinance) (0.0.11)\n","Requirement already satisfied: pandas>=1.3.0 in /usr/local/lib/python3.9/dist-packages (from yfinance) (1.4.4)\n","Requirement already satisfied: lxml>=4.9.1 in /usr/local/lib/python3.9/dist-packages (from yfinance) (4.9.2)\n","Requirement already satisfied: requests>=2.26 in /usr/local/lib/python3.9/dist-packages (from yfinance) (2.27.1)\n","Requirement already satisfied: numpy>=1.16.5 in /usr/local/lib/python3.9/dist-packages (from yfinance) (1.22.4)\n","Requirement already satisfied: appdirs>=1.4.4 in /usr/local/lib/python3.9/dist-packages (from yfinance) (1.4.4)\n","Requirement already satisfied: cryptography>=3.3.2 in /usr/local/lib/python3.9/dist-packages (from yfinance) (39.0.2)\n","Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.9/dist-packages (from beautifulsoup4>=4.11.1->yfinance) (2.4)\n","Requirement already satisfied: cffi>=1.12 in /usr/local/lib/python3.9/dist-packages (from cryptography>=3.3.2->yfinance) (1.15.1)\n","Requirement already satisfied: six>=1.9 in /usr/local/lib/python3.9/dist-packages (from html5lib>=1.1->yfinance) (1.16.0)\n","Requirement already satisfied: webencodings in /usr/local/lib/python3.9/dist-packages (from html5lib>=1.1->yfinance) (0.5.1)\n","Requirement already satisfied: python-dateutil>=2.8.1 in /usr/local/lib/python3.9/dist-packages (from pandas>=1.3.0->yfinance) (2.8.2)\n","Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/local/lib/python3.9/dist-packages (from requests>=2.26->yfinance) (2.0.12)\n","Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.9/dist-packages (from requests>=2.26->yfinance) (3.4)\n","Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.9/dist-packages (from requests>=2.26->yfinance) (2022.12.7)\n","Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.9/dist-packages (from requests>=2.26->yfinance) (1.26.15)\n","Requirement already satisfied: pycparser in /usr/local/lib/python3.9/dist-packages (from cffi>=1.12->cryptography>=3.3.2->yfinance) (2.21)\n","Name: yfinance\n","Version: 0.2.13\n","Summary: Download market data from Yahoo! Finance API\n","Home-page: https://github.com/ranaroussi/yfinance\n","Author: Ran Aroussi\n","Author-email: ran@aroussi.com\n","License: Apache\n","Location: /usr/local/lib/python3.9/dist-packages\n","Requires: appdirs, beautifulsoup4, cryptography, frozendict, html5lib, lxml, multitasking, numpy, pandas, pytz, requests\n","Required-by: \n"]}]},{"cell_type":"code","execution_count":2,"metadata":{"id":"lQNFMoqDNptL","executionInfo":{"status":"ok","timestamp":1679926904728,"user_tz":-480,"elapsed":2852,"user":{"displayName":"Tan Jun Xuan","userId":"00319716665018572021"}}},"outputs":[],"source":["import pandas_datareader.data as reader\n","import matplotlib.pyplot as plt\n","import datetime as dt\n","import seaborn as sns\n","import yfinance as yf"]},{"cell_type":"code","source":["end = dt.datetime.now()\n","start = dt.date(end.year - 1, end.month, end.day)"],"metadata":{"id":"y6_IAIbRSUf0","executionInfo":{"status":"ok","timestamp":1679926904729,"user_tz":-480,"elapsed":10,"user":{"displayName":"Tan Jun Xuan","userId":"00319716665018572021"}}},"execution_count":3,"outputs":[]},{"cell_type":"code","source":["portfolio = ['QQQ', 'TQQQ', 'SQQQ', '^GSPC']"],"metadata":{"id":"sNsSjCD-T6Ex","executionInfo":{"status":"ok","timestamp":1679926904729,"user_tz":-480,"elapsed":9,"user":{"displayName":"Tan Jun Xuan","userId":"00319716665018572021"}}},"execution_count":4,"outputs":[]},{"cell_type":"code","source":["# df = reader.get_data_yahoo(portfolio,start,end)\n","df = yf.download(portfolio, start=start, end=end)['Adj Close']\n","# df = yf.download(['GOOG', 'AAPL', 'MSFT', 'TSLA', '^GSPC'], start=start, end=end)['Adj Close']"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"g_NkKrrJVgO2","executionInfo":{"status":"ok","timestamp":1679926906958,"user_tz":-480,"elapsed":2237,"user":{"displayName":"Tan Jun Xuan","userId":"00319716665018572021"}},"outputId":"77d492f7-6ba0-4ec7-df7c-b95761b1c32f"},"execution_count":5,"outputs":[{"output_type":"stream","name":"stdout","text":["[*********************100%***********************]  4 of 4 completed\n"]}]},{"cell_type":"code","source":["df"],"metadata":{"id":"XOFWgrO4V6h2","colab":{"base_uri":"https://localhost:8080/","height":455},"executionInfo":{"status":"ok","timestamp":1679926906959,"user_tz":-480,"elapsed":33,"user":{"displayName":"Tan Jun Xuan","userId":"00319716665018572021"}},"outputId":"ca8d712e-b694-4038-8e53-00ae8f708ec3"},"execution_count":6,"outputs":[{"output_type":"execute_result","data":{"text/plain":["                   QQQ       SQQQ       TQQQ        ^GSPC\n","Date                                                     \n","2022-03-28  362.127655  32.755379  58.869488  4575.520020\n","2022-03-29  368.359741  31.080954  61.886150  4631.600098\n","2022-03-30  364.291016  32.022198  60.026695  4602.450195\n","2022-03-31  359.775726  33.359756  57.544132  4530.410156\n","2022-04-01  359.090973  33.468746  57.296864  4545.859863\n","...                ...        ...        ...          ...\n","2023-03-21  310.339996  32.536003  25.730000  4002.870117\n","2023-03-22  306.119995  33.860001  24.680000  3936.969971\n","2023-03-23  309.750000  32.689999  25.559999  3948.719971\n","2023-03-24  310.890015  32.340000  25.820000  3970.989990\n","2023-03-27  311.589996  32.139999  25.975000  3991.570068\n","\n","[251 rows x 4 columns]"],"text/html":["\n","  <div id=\"df-8c655010-2dca-40a1-80e7-883b624c6530\">\n","    <div class=\"colab-df-container\">\n","      <div>\n","<style scoped>\n","    .dataframe tbody tr th:only-of-type {\n","        vertical-align: middle;\n","    }\n","\n","    .dataframe tbody tr th {\n","        vertical-align: top;\n","    }\n","\n","    .dataframe thead th {\n","        text-align: right;\n","    }\n","</style>\n","<table border=\"1\" class=\"dataframe\">\n","  <thead>\n","    <tr style=\"text-align: right;\">\n","      <th></th>\n","      <th>QQQ</th>\n","      <th>SQQQ</th>\n","      <th>TQQQ</th>\n","      <th>^GSPC</th>\n","    </tr>\n","    <tr>\n","      <th>Date</th>\n","      <th></th>\n","      <th></th>\n","      <th></th>\n","      <th></th>\n","    </tr>\n","  </thead>\n","  <tbody>\n","    <tr>\n","      <th>2022-03-28</th>\n","      <td>362.127655</td>\n","      <td>32.755379</td>\n","      <td>58.869488</td>\n","      <td>4575.520020</td>\n","    </tr>\n","    <tr>\n","      <th>2022-03-29</th>\n","      <td>368.359741</td>\n","      <td>31.080954</td>\n","      <td>61.886150</td>\n","      <td>4631.600098</td>\n","    </tr>\n","    <tr>\n","      <th>2022-03-30</th>\n","      <td>364.291016</td>\n","      <td>32.022198</td>\n","      <td>60.026695</td>\n","      <td>4602.450195</td>\n","    </tr>\n","    <tr>\n","      <th>2022-03-31</th>\n","      <td>359.775726</td>\n","      <td>33.359756</td>\n","      <td>57.544132</td>\n","      <td>4530.410156</td>\n","    </tr>\n","    <tr>\n","      <th>2022-04-01</th>\n","      <td>359.090973</td>\n","      <td>33.468746</td>\n","      <td>57.296864</td>\n","      <td>4545.859863</td>\n","    </tr>\n","    <tr>\n","      <th>...</th>\n","      <td>...</td>\n","      <td>...</td>\n","      <td>...</td>\n","      <td>...</td>\n","    </tr>\n","    <tr>\n","      <th>2023-03-21</th>\n","      <td>310.339996</td>\n","      <td>32.536003</td>\n","      <td>25.730000</td>\n","      <td>4002.870117</td>\n","    </tr>\n","    <tr>\n","      <th>2023-03-22</th>\n","      <td>306.119995</td>\n","      <td>33.860001</td>\n","      <td>24.680000</td>\n","      <td>3936.969971</td>\n","    </tr>\n","    <tr>\n","      <th>2023-03-23</th>\n","      <td>309.750000</td>\n","      <td>32.689999</td>\n","      <td>25.559999</td>\n","      <td>3948.719971</td>\n","    </tr>\n","    <tr>\n","      <th>2023-03-24</th>\n","      <td>310.890015</td>\n","      <td>32.340000</td>\n","      <td>25.820000</td>\n","      <td>3970.989990</td>\n","    </tr>\n","    <tr>\n","      <th>2023-03-27</th>\n","      <td>311.589996</td>\n","      <td>32.139999</td>\n","      <td>25.975000</td>\n","      <td>3991.570068</td>\n","    </tr>\n","  </tbody>\n","</table>\n","<p>251 rows × 4 columns</p>\n","</div>\n","      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-8c655010-2dca-40a1-80e7-883b624c6530')\"\n","              title=\"Convert this dataframe to an interactive table.\"\n","              style=\"display:none;\">\n","        \n","  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n","       width=\"24px\">\n","    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n","    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n","  </svg>\n","      </button>\n","      \n","  <style>\n","    .colab-df-container {\n","      display:flex;\n","      flex-wrap:wrap;\n","      gap: 12px;\n","    }\n","\n","    .colab-df-convert {\n","      background-color: #E8F0FE;\n","      border: none;\n","      border-radius: 50%;\n","      cursor: pointer;\n","      display: none;\n","      fill: #1967D2;\n","      height: 32px;\n","      padding: 0 0 0 0;\n","      width: 32px;\n","    }\n","\n","    .colab-df-convert:hover {\n","      background-color: #E2EBFA;\n","      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n","      fill: #174EA6;\n","    }\n","\n","    [theme=dark] .colab-df-convert {\n","      background-color: #3B4455;\n","      fill: #D2E3FC;\n","    }\n","\n","    [theme=dark] .colab-df-convert:hover {\n","      background-color: #434B5C;\n","      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n","      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n","      fill: #FFFFFF;\n","    }\n","  </style>\n","\n","      <script>\n","        const buttonEl =\n","          document.querySelector('#df-8c655010-2dca-40a1-80e7-883b624c6530 button.colab-df-convert');\n","        buttonEl.style.display =\n","          google.colab.kernel.accessAllowed ? 'block' : 'none';\n","\n","        async function convertToInteractive(key) {\n","          const element = document.querySelector('#df-8c655010-2dca-40a1-80e7-883b624c6530');\n","          const dataTable =\n","            await google.colab.kernel.invokeFunction('convertToInteractive',\n","                                                     [key], {});\n","          if (!dataTable) return;\n","\n","          const docLinkHtml = 'Like what you see? Visit the ' +\n","            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n","            + ' to learn more about interactive tables.';\n","          element.innerHTML = '';\n","          dataTable['output_type'] = 'display_data';\n","          await google.colab.output.renderOutput(dataTable, element);\n","          const docLink = document.createElement('div');\n","          docLink.innerHTML = docLinkHtml;\n","          element.appendChild(docLink);\n","        }\n","      </script>\n","    </div>\n","  </div>\n","  "]},"metadata":{},"execution_count":6}]},{"cell_type":"code","source":["returns = df.pct_change()"],"metadata":{"id":"Sl626mCMVyee","executionInfo":{"status":"ok","timestamp":1679926906960,"user_tz":-480,"elapsed":29,"user":{"displayName":"Tan Jun Xuan","userId":"00319716665018572021"}}},"execution_count":7,"outputs":[]},{"cell_type":"code","source":["returns.cov()"],"metadata":{"colab":{"base_uri":"https://localhost:8080/","height":175},"id":"AIVXOjWCWvWo","executionInfo":{"status":"ok","timestamp":1679926906961,"user_tz":-480,"elapsed":29,"user":{"displayName":"Tan Jun Xuan","userId":"00319716665018572021"}},"outputId":"8c67f715-2f87-4851-d7f8-a9c392e2cb44"},"execution_count":8,"outputs":[{"output_type":"execute_result","data":{"text/plain":["            QQQ      SQQQ      TQQQ     ^GSPC\n","QQQ    0.000369 -0.001096  0.001095  0.000272\n","SQQQ  -0.001096  0.003257 -0.003256 -0.000809\n","TQQQ   0.001095 -0.003256  0.003256  0.000809\n","^GSPC  0.000272 -0.000809  0.000809  0.000216"],"text/html":["\n","  <div id=\"df-48f98b76-a509-4451-8f0a-6a41bc11c2ef\">\n","    <div class=\"colab-df-container\">\n","      <div>\n","<style scoped>\n","    .dataframe tbody tr th:only-of-type {\n","        vertical-align: middle;\n","    }\n","\n","    .dataframe tbody tr th {\n","        vertical-align: top;\n","    }\n","\n","    .dataframe thead th {\n","        text-align: right;\n","    }\n","</style>\n","<table border=\"1\" class=\"dataframe\">\n","  <thead>\n","    <tr style=\"text-align: right;\">\n","      <th></th>\n","      <th>QQQ</th>\n","      <th>SQQQ</th>\n","      <th>TQQQ</th>\n","      <th>^GSPC</th>\n","    </tr>\n","  </thead>\n","  <tbody>\n","    <tr>\n","      <th>QQQ</th>\n","      <td>0.000369</td>\n","      <td>-0.001096</td>\n","      <td>0.001095</td>\n","      <td>0.000272</td>\n","    </tr>\n","    <tr>\n","      <th>SQQQ</th>\n","      <td>-0.001096</td>\n","      <td>0.003257</td>\n","      <td>-0.003256</td>\n","      <td>-0.000809</td>\n","    </tr>\n","    <tr>\n","      <th>TQQQ</th>\n","      <td>0.001095</td>\n","      <td>-0.003256</td>\n","      <td>0.003256</td>\n","      <td>0.000809</td>\n","    </tr>\n","    <tr>\n","      <th>^GSPC</th>\n","      <td>0.000272</td>\n","      <td>-0.000809</td>\n","      <td>0.000809</td>\n","      <td>0.000216</td>\n","    </tr>\n","  </tbody>\n","</table>\n","</div>\n","      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-48f98b76-a509-4451-8f0a-6a41bc11c2ef')\"\n","              title=\"Convert this dataframe to an interactive table.\"\n","              style=\"display:none;\">\n","        \n","  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n","       width=\"24px\">\n","    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n","    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n","  </svg>\n","      </button>\n","      \n","  <style>\n","    .colab-df-container {\n","      display:flex;\n","      flex-wrap:wrap;\n","      gap: 12px;\n","    }\n","\n","    .colab-df-convert {\n","      background-color: #E8F0FE;\n","      border: none;\n","      border-radius: 50%;\n","      cursor: pointer;\n","      display: none;\n","      fill: #1967D2;\n","      height: 32px;\n","      padding: 0 0 0 0;\n","      width: 32px;\n","    }\n","\n","    .colab-df-convert:hover {\n","      background-color: #E2EBFA;\n","      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n","      fill: #174EA6;\n","    }\n","\n","    [theme=dark] .colab-df-convert {\n","      background-color: #3B4455;\n","      fill: #D2E3FC;\n","    }\n","\n","    [theme=dark] .colab-df-convert:hover {\n","      background-color: #434B5C;\n","      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n","      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n","      fill: #FFFFFF;\n","    }\n","  </style>\n","\n","      <script>\n","        const buttonEl =\n","          document.querySelector('#df-48f98b76-a509-4451-8f0a-6a41bc11c2ef button.colab-df-convert');\n","        buttonEl.style.display =\n","          google.colab.kernel.accessAllowed ? 'block' : 'none';\n","\n","        async function convertToInteractive(key) {\n","          const element = document.querySelector('#df-48f98b76-a509-4451-8f0a-6a41bc11c2ef');\n","          const dataTable =\n","            await google.colab.kernel.invokeFunction('convertToInteractive',\n","                                                     [key], {});\n","          if (!dataTable) return;\n","\n","          const docLinkHtml = 'Like what you see? Visit the ' +\n","            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n","            + ' to learn more about interactive tables.';\n","          element.innerHTML = '';\n","          dataTable['output_type'] = 'display_data';\n","          await google.colab.output.renderOutput(dataTable, element);\n","          const docLink = document.createElement('div');\n","          docLink.innerHTML = docLinkHtml;\n","          element.appendChild(docLink);\n","        }\n","      </script>\n","    </div>\n","  </div>\n","  "]},"metadata":{},"execution_count":8}]},{"cell_type":"code","source":["returns.var()"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"WJuLEsXnZz8e","executionInfo":{"status":"ok","timestamp":1679926906962,"user_tz":-480,"elapsed":29,"user":{"displayName":"Tan Jun Xuan","userId":"00319716665018572021"}},"outputId":"ad4c8fae-c18d-47ba-9ac5-cec4d866ff79"},"execution_count":9,"outputs":[{"output_type":"execute_result","data":{"text/plain":["QQQ      0.000369\n","SQQQ     0.003257\n","TQQQ     0.003256\n","^GSPC    0.000216\n","dtype: float64"]},"metadata":{},"execution_count":9}]},{"cell_type":"code","source":["returns.corr()"],"metadata":{"colab":{"base_uri":"https://localhost:8080/","height":175},"id":"qyUsgr0xaT4j","executionInfo":{"status":"ok","timestamp":1679927490339,"user_tz":-480,"elapsed":1440,"user":{"displayName":"Tan Jun Xuan","userId":"00319716665018572021"}},"outputId":"bb5481c7-a0cc-47cf-c7cd-2332bd4cb469"},"execution_count":12,"outputs":[{"output_type":"execute_result","data":{"text/plain":["            QQQ      SQQQ      TQQQ     ^GSPC\n","QQQ    1.000000 -0.999715  0.999754  0.964087\n","SQQQ  -0.999715  1.000000 -0.999800 -0.964606\n","TQQQ   0.999754 -0.999800  1.000000  0.964187\n","^GSPC  0.964087 -0.964606  0.964187  1.000000"],"text/html":["\n","  <div id=\"df-12a77c7f-817d-4ac0-9628-7d0aabd28bbe\">\n","    <div class=\"colab-df-container\">\n","      <div>\n","<style scoped>\n","    .dataframe tbody tr th:only-of-type {\n","        vertical-align: middle;\n","    }\n","\n","    .dataframe tbody tr th {\n","        vertical-align: top;\n","    }\n","\n","    .dataframe thead th {\n","        text-align: right;\n","    }\n","</style>\n","<table border=\"1\" class=\"dataframe\">\n","  <thead>\n","    <tr style=\"text-align: right;\">\n","      <th></th>\n","      <th>QQQ</th>\n","      <th>SQQQ</th>\n","      <th>TQQQ</th>\n","      <th>^GSPC</th>\n","    </tr>\n","  </thead>\n","  <tbody>\n","    <tr>\n","      <th>QQQ</th>\n","      <td>1.000000</td>\n","      <td>-0.999715</td>\n","      <td>0.999754</td>\n","      <td>0.964087</td>\n","    </tr>\n","    <tr>\n","      <th>SQQQ</th>\n","      <td>-0.999715</td>\n","      <td>1.000000</td>\n","      <td>-0.999800</td>\n","      <td>-0.964606</td>\n","    </tr>\n","    <tr>\n","      <th>TQQQ</th>\n","      <td>0.999754</td>\n","      <td>-0.999800</td>\n","      <td>1.000000</td>\n","      <td>0.964187</td>\n","    </tr>\n","    <tr>\n","      <th>^GSPC</th>\n","      <td>0.964087</td>\n","      <td>-0.964606</td>\n","      <td>0.964187</td>\n","      <td>1.000000</td>\n","    </tr>\n","  </tbody>\n","</table>\n","</div>\n","      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-12a77c7f-817d-4ac0-9628-7d0aabd28bbe')\"\n","              title=\"Convert this dataframe to an interactive table.\"\n","              style=\"display:none;\">\n","        \n","  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n","       width=\"24px\">\n","    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n","    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n","  </svg>\n","      </button>\n","      \n","  <style>\n","    .colab-df-container {\n","      display:flex;\n","      flex-wrap:wrap;\n","      gap: 12px;\n","    }\n","\n","    .colab-df-convert {\n","      background-color: #E8F0FE;\n","      border: none;\n","      border-radius: 50%;\n","      cursor: pointer;\n","      display: none;\n","      fill: #1967D2;\n","      height: 32px;\n","      padding: 0 0 0 0;\n","      width: 32px;\n","    }\n","\n","    .colab-df-convert:hover {\n","      background-color: #E2EBFA;\n","      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n","      fill: #174EA6;\n","    }\n","\n","    [theme=dark] .colab-df-convert {\n","      background-color: #3B4455;\n","      fill: #D2E3FC;\n","    }\n","\n","    [theme=dark] .colab-df-convert:hover {\n","      background-color: #434B5C;\n","      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n","      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n","      fill: #FFFFFF;\n","    }\n","  </style>\n","\n","      <script>\n","        const buttonEl =\n","          document.querySelector('#df-12a77c7f-817d-4ac0-9628-7d0aabd28bbe button.colab-df-convert');\n","        buttonEl.style.display =\n","          google.colab.kernel.accessAllowed ? 'block' : 'none';\n","\n","        async function convertToInteractive(key) {\n","          const element = document.querySelector('#df-12a77c7f-817d-4ac0-9628-7d0aabd28bbe');\n","          const dataTable =\n","            await google.colab.kernel.invokeFunction('convertToInteractive',\n","                                                     [key], {});\n","          if (!dataTable) return;\n","\n","          const docLinkHtml = 'Like what you see? Visit the ' +\n","            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n","            + ' to learn more about interactive tables.';\n","          element.innerHTML = '';\n","          dataTable['output_type'] = 'display_data';\n","          await google.colab.output.renderOutput(dataTable, element);\n","          const docLink = document.createElement('div');\n","          docLink.innerHTML = docLinkHtml;\n","          element.appendChild(docLink);\n","        }\n","      </script>\n","    </div>\n","  </div>\n","  "]},"metadata":{},"execution_count":12}]},{"cell_type":"code","source":["sns.heatmap(returns.corr())"],"metadata":{"colab":{"base_uri":"https://localhost:8080/","height":286},"id":"10iHusrBaZbD","executionInfo":{"status":"ok","timestamp":1679926906964,"user_tz":-480,"elapsed":26,"user":{"displayName":"Tan Jun Xuan","userId":"00319716665018572021"}},"outputId":"268bb7c7-3f62-412b-efd0-92407646cb88"},"execution_count":11,"outputs":[{"output_type":"execute_result","data":{"text/plain":["<Axes: >"]},"metadata":{},"execution_count":11},{"output_type":"display_data","data":{"text/plain":["<Figure size 432x288 with 2 Axes>"],"image/png":"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\n"},"metadata":{"needs_background":"light"}}]}]}