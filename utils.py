def get_his_data_filename(pair, granularity):
    return f"downloadeddata/{pair}_{granularity}.pkl"


def get_instruments_data_filename():
    return "instrument.pkl"
