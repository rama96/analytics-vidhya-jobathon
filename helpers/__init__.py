import warnings
from pathlib import Path
import os
import pandas as pd
from datetime import datetime , timedelta

today_time = datetime.today() + timedelta(days = 1)

TODAY = today_time.strftime('%Y-%m-%d')
TODAY_SUFFIX = today_time.strftime('%Y%m%d')

warnings.simplefilter(action="ignore", category=FutureWarning)

warnings.simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

# your performance may suffer as PyTables will pickle object types that it cannot

def create_directory_if_not_exists(path: Path) -> None:
    if not path.is_dir():
        try:
            path.mkdir()
        except Exception as e:
            print(e)


DIR_PACKAGE = Path(__file__).resolve().parent  # ../analytics-vidhya-jobathon/helpers
DIR_BASE = DIR_PACKAGE.parent  # ../analytics-vidhya-jobathon

# ../analytics-vidhya-jobathon/DATA
DIR_DATA = DIR_BASE.joinpath("DATA")


name = "analytics-vidhya-jobathon"

pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)
pd.set_option("display.max_colwidth", 25)
pd.options.display.float_format = "{:.2f}".format
pd.options.mode.chained_assignment = None

