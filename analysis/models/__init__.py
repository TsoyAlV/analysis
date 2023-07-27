import pandas as pd


def catboost_forecast(xtrain, ytrain, xtest, ytest):
    import catboost
    model = catboost.CatBoostRegressor(iterations=900,
                                       learning_rate=0.1,
                                       depth=7)
    model.fit(xtrain, ytrain, plot=True, verbose=False)
    df_res = ytest.copy()
    df_res['predict'] = model.predict(xtest)
    df_res['err'] = df_res.TS_T1_obr - df_res.predict
    df_res['err_abs'] = df_res['err'].abs()
    return df_res


def LGBM_forecast(xtrain, ytrain, xtest, ytest):
    import lightgbm as lgbm
    model = lgbm.LGBMRegressor()
    model.fit(xtrain, ytrain)
    df_res = ytest.copy()
    df_res['predict'] = model.predict(xtest)
    df_res['err'] = df_res.TS_T1_obr - df_res.predict
    df_res['err_abs'] = df_res['err'].abs()
    return df_res


def LinearRegression_forecast(xtrain, ytrain, xtest, ytest):
    from sklearn.linear_model import LinearRegression
    model1 = LinearRegression()
    model1.fit(xtrain, ytrain)
    df_res = ytest.copy()
    df_res['predict'] = model1.predict(xtest)
    df_res['err'] = df_res.TS_T1_obr - df_res.predict
    df_res['err_abs'] = df_res['err'].abs()
    return df_res


def Ridge_forecast(xtrain, ytrain, xtest, ytest):
    from sklearn.linear_model import Ridge
    model = Ridge()
    model.fit(xtrain, ytrain)
    df_res = ytest.copy()
    df_res['predict'] = model.predict(xtest)
    df_res['err'] = df_res.TS_T1_obr - df_res.predict
    df_res['err_abs'] = df_res['err'].abs()
    return df_res
