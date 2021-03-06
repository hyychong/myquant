import numpy as np
import matplotlib.pyplot as plt
from matplotlib.finance import *
from myquant.finance import *
from myquant.fracdiff import *
from myquant.nnet.pyNet import *

shapes = np.array([[  2.,  20.,   0.,   0.],
                   [ 20.,   0.,   0.,   0.],
                   [ 20.,  20.,   0.,   0.],
                   [ 20.,   0.,   0.,   0.],
                   [ 20.,   1.,   0.,   0.],
                   [  1.,   0.,   0.,   0.]])

pars = np.array([ -4.69232804e-01,  -6.24909579e-02,  -9.61261438e-01,
                 -3.15328144e-01,  -3.49333210e-01,  -8.92520072e-01,
                 8.50460501e-01,  -7.14211663e-01,   2.54610141e-01,
                 1.09827329e+00,  -7.61612729e-01,  -7.00090746e-02,
                 4.77323574e-01,   1.02782812e+00,   1.02045043e-01,
                -4.21036846e-01,  -3.38596056e-01,  -7.05494057e-02,
                 1.12382233e-01,  -1.00557693e-01,  -6.44157157e-02,
                 4.20306144e-01,   5.72590771e-01,  -2.39194592e-01,
                 1.26325761e-02,  -3.30030218e-01,  -1.65131145e-01,
                -7.38700931e-01,   1.85099701e-02,   3.10262157e-01,
                 7.15754245e-01,   8.02936991e-01,  -9.71734176e-01,
                 1.01925621e+00,   7.46927257e-01,  -8.47395085e-01,
                 2.40853050e-01,   6.30793046e-01,  -3.39215370e-01,
                -1.26667566e-01,  -5.84826238e-02,  -2.02933371e-01,
                -2.46718041e-01,  -1.24430675e-01,  -5.00962132e-02,
                 2.58897289e-01,  -1.51615314e-01,   1.24929026e-01,
                -1.03589192e+00,   4.52573934e-01,   6.19937002e-02,
                -1.05541053e+00,  -2.89431706e-01,  -1.95607360e-01,
                -3.77009301e-01,   4.71119926e-01,  -2.24456623e-01,
                -9.64449121e-01,  -6.29095237e-01,  -1.08135280e+00,
                -4.28391997e-01,  -1.00537065e-04,  -8.53517625e-01,
                -2.78079147e-01,  -3.19703358e-01,  -2.80351052e-01,
                 2.65577605e-01,  -6.21848879e-01,   8.70832044e-01,
                 4.85200286e-01,  -6.22227253e-01,   5.55879615e-01,
                 6.96146055e-01,   9.49531749e-01,   2.85197737e-01,
                -1.07452004e-02,  -2.62044414e-01,   5.24218782e-01,
                 5.21051968e-01,   4.72127159e-01,  -8.70892297e-02,
                 4.56554809e-01,   5.74117592e-01,  -2.69786875e-01,
                 5.34347950e-03,  -3.96142908e-01,  -3.11091694e-01,
                -7.86136430e-01,  -6.32192595e-02,  -6.49494134e-02,
                 6.70601631e-01,   8.81556198e-01,  -8.83558343e-01,
                 7.86598022e-01,   7.83374543e-01,  -6.30083250e-01,
                 3.11195903e-01,   6.16395893e-01,  -4.87018145e-01,
                -2.84228707e-01,  -3.27599172e-01,   4.98815486e-01,
                -2.96296210e-01,  -2.94066997e-01,   5.95910363e-01,
                 3.48777847e-01,   5.38563456e-01,  -9.27168429e-01,
                 6.76326907e-01,  -2.29527910e-01,   9.92087601e-01,
                -2.41350727e-01,   4.73760859e-01,  -7.39345695e-01,
                 5.50584347e-01,   8.88129965e-01,   3.70939409e-01,
                 4.84936082e-02,   2.15475239e-01,  -7.02810368e-01,
                 7.61653935e-02,   8.08739020e-01,  -2.79835955e-01,
                -9.61472426e-01,  -8.21975656e-01,  -4.76969149e-01,
                 8.41845050e-01,   7.77956987e-01,  -2.80973379e-01,
                 3.48815639e-02,   2.42272894e-01,   1.80096151e-01,
                 6.24779615e-01,  -6.55525053e-02,  -9.76996739e-01,
                 8.61617632e-02,   2.62268419e-01,   3.44754282e-01,
                -9.21196880e-01,   3.02442764e-01,  -8.39422348e-01,
                 6.08577179e-01,   8.28802602e-01,  -4.98508863e-01,
                -6.93915662e-01,   1.75864446e-01,  -7.02626108e-01,
                -7.34671381e-02,  -5.31744834e-01,  -6.36397090e-01,
                -6.07444518e-01,  -1.90454251e-01,  -6.62131817e-01,
                 3.83071913e-01,  -3.82544251e-01,  -6.96617568e-01,
                -9.35033247e-01,  -8.31044929e-01,   4.79649749e-01,
                -9.70615751e-01,   8.44837424e-01,   2.56373897e-01,
                 5.20963216e-02,  -3.69137468e-01,  -3.56652722e-01,
                -1.19151765e+00,   4.20584917e-01,   1.71546645e-01,
                -1.79626781e-01,  -9.74962573e-01,  -2.98329559e-01,
                -9.66176465e-01,   6.78632461e-01,  -9.57636123e-01,
                -2.17801328e-02,   2.52724262e-01,  -1.42689039e-01,
                -7.86901285e-01,  -5.32391678e-01,  -4.84580856e-01,
                -1.94525391e-03,  -3.63030169e-01,   9.48968556e-01,
                 3.05762699e-01,  -6.50400538e-01,  -9.13936685e-01,
                -6.55247610e-02,  -1.28211308e+00,   5.20928580e-02,
                -7.87666863e-01,   2.12498251e-01,   4.60325733e-01,
                 7.95693860e-01,  -4.93719152e-01,  -9.50535176e-01,
                -1.13491479e+00,  -5.05970387e-01,   1.51676951e-01,
                -8.56013638e-01,  -9.30055252e-02,   7.84657738e-01,
                -7.60872757e-01,   9.20723143e-01,  -2.41879192e-02,
                 6.37436026e-01,   6.01158458e-01,  -5.03845406e-01,
                 1.36747511e-01,  -6.36878870e-01,  -4.87039928e-01,
                 9.81949653e-01,  -5.52062255e-01,  -3.08610190e-01,
                 1.99136450e-01,  -1.70255758e-01,  -1.06961222e-01,
                -9.45861262e-02,   3.91449268e-01,   3.37438014e-01,
                -8.76327902e-01,   6.75181616e-01,  -6.90053555e-01,
                -8.54512298e-01,  -8.03483516e-01,   8.06346358e-01,
                 7.57674061e-01,   8.07977950e-01,   4.79491380e-01,
                 7.97583735e-01,   7.40921549e-01,  -5.83163370e-01,
                 2.59476422e-01,  -6.60542691e-01,   1.55082163e-01,
                -7.82357947e-01,   7.91291115e-01,   4.48396454e-01,
                -3.20757368e-01,   6.79904156e-01,  -6.50297990e-01,
                 8.25461175e-01,   4.88594026e-01,   2.46158844e-01,
                -4.38772560e-02,   3.00614888e-02,   9.05387169e-01,
                -2.32355198e-01,  -1.04309690e+00,  -4.66243467e-01,
                -1.01397109e+00,  -9.43869716e-01,  -9.50763509e-01,
                -3.68937190e-01,  -6.45692633e-01,   8.56626382e-01,
                -5.70214612e-01,   8.24745850e-01,   4.57919416e-01,
                -9.87877271e-01,  -9.10953881e-01,   9.76816558e-01,
                 2.00779206e-01,   4.78516180e-01,   5.14291011e-01,
                 2.32741749e-01,   1.60247124e-01,   3.09999202e-01,
                -9.83468375e-01,  -4.97693137e-01,   7.67529361e-01,
                 6.80661019e-02,   2.64133601e-01,  -8.68311474e-01,
                -6.58980096e-01,  -3.41937159e-01,  -1.21496343e-01,
                -3.26777162e-01,   3.95675350e-01,   5.93455144e-01,
                -1.22533069e-01,   6.75994317e-01,   7.99262792e-01,
                 1.05821944e-01,   1.20045406e-01,   7.94800444e-01,
                 4.65284822e-01,  -8.21095339e-01,   6.03789259e-01,
                 1.16884859e-01,  -1.66251545e-01,   4.71424926e-01,
                -7.10218585e-01,  -9.82197606e-02,   3.16166109e-01,
                -6.41622594e-01,  -6.83983885e-01,  -1.03545538e-01,
                 7.96939492e-04,   1.05449889e-01,   7.13526447e-01,
                 2.42611858e-01,   3.45137844e-01,  -2.31380038e-01,
                 3.61735950e-01,  -1.10318475e-01,  -6.06091262e-01,
                 5.56424982e-01,   7.68485779e-01,  -1.26554867e-01,
                 1.25881495e-01,   1.74326088e-01,   5.91301348e-01,
                 8.26331258e-01,  -9.77519667e-01,  -2.85880178e-02,
                 5.03360556e-02,   2.81816904e-01,   6.39403125e-02,
                 1.27548174e-02,  -8.48795076e-01,  -1.02283923e+00,
                -4.91349605e-01,  -2.35618678e-01,   3.38775515e-01,
                 7.40376992e-02,   4.51144878e-01,  -2.42761592e-01,
                -1.64707476e+00,  -8.26817046e-01,  -9.77478191e-03,
                -3.57438770e-01,  -4.28332788e-01,  -9.37894671e-01,
                -3.95454599e-01,  -2.36497969e-02,   1.21249230e-01,
                 1.14433368e-01,  -3.38781600e-01,  -1.06016583e+00,
                -5.07462347e-01,  -3.70866170e-01,   2.71424818e-01,
                 1.38998374e-01,  -3.47772714e-01,   1.91240001e-01,
                -4.43612350e-01,   7.96071198e-01,   1.43960081e-01,
                -2.36926027e-01,   2.99280653e-01,   4.07104275e-01,
                -2.86466174e-02,   6.53647704e-01,  -7.87875189e-01,
                 3.29565902e-01,   2.93894492e-01,   9.22453672e-01,
                -5.48039402e-02,  -7.29301295e-01,   4.43344738e-01,
                 1.08610392e-01,   7.08513706e-01,  -6.61403051e-01,
                 9.86193514e-02,   1.04668837e-01,  -9.90715785e-01,
                 2.96437249e-01,  -2.94988395e-01,   8.98323331e-02,
                 1.80895287e-01,   6.57242287e-01,  -9.51034719e-02,
                -2.18211619e-01,  -3.60582336e-01,  -9.72550434e-01,
                 1.32387613e-01,  -8.29441294e-01,  -6.69082407e-02,
                 7.34656535e-01,  -2.43263945e-01,  -8.96616135e-01,
                -2.49169913e-01,   9.94967216e-01,   4.33441234e-01,
                 8.23482451e-01,   9.32241666e-01,   2.43090882e-01,
                -2.76100451e-01,   7.14228016e-01,  -4.44833287e-01,
                -6.16880204e-01,  -7.42600218e-01,   3.97957672e-02,
                 8.42414539e-01,  -4.83976393e-01,   5.85690923e-01,
                -7.57881967e-01,  -8.13780822e-01,   9.22646010e-01,
                -3.37948614e-01,   3.33143241e-01,  -6.65560984e-01,
                 8.50069551e-01,   3.76915071e-01,  -8.04518794e-01,
                -5.92839714e-01,  -6.56048848e-01,   4.61535421e-01,
                -8.48016791e-01,   1.76498387e-01,   4.93102136e-01,
                -4.60055050e-01,   3.59579201e-01,   1.78190687e-02,
                 6.04506174e-01,   7.80257108e-01,   4.16721711e-01,
                -3.75938333e-02,  -1.00966885e+00,   2.95561350e-01,
                -5.32064159e-01,   1.03989077e-01,  -7.25581707e-01,
                -6.58531640e-01,  -4.28544448e-01,   8.32036427e-01,
                -5.06532356e-01,   6.89760224e-01,  -2.97557295e-01,
                -1.25912621e-01,   7.23119796e-01,  -5.51390315e-01,
                -7.78363678e-01,   8.68830262e-01,  -5.69268790e-02,
                -2.61926319e-01,  -2.56061107e-01,   6.45189689e-01,
                 7.35931665e-01,   1.79343366e-01,   4.66012517e-01,
                 1.73071679e-01,  -8.17964866e-01,   6.67040566e-01,
                -7.05315438e-01,  -4.75670992e-01,  -5.22183873e-01,
                 5.02258738e-01,   4.40335028e-01,  -6.81521475e-01,
                 8.97966604e-01,   1.39108038e-01,  -4.22606589e-01,
                 5.83696743e-02,   8.25886699e-01,   2.09308556e-01,
                 5.29526481e-02,   4.00262175e-01,  -8.59786685e-01,
                -2.30602425e-01,  -3.15810924e-01,  -3.64718693e-01,
                -4.72257536e-01,  -7.27629749e-01,  -2.95165193e-01,
                 3.36090919e-02,  -1.44105312e-01,  -9.07378953e-01,
                -8.87020089e-01,   1.07436173e-02,  -5.37838431e-01,
                -4.22653837e-02,  -2.07542247e-01,  -1.43989130e-01,
                -3.43518129e-01,  -7.29016552e-01,   5.17366935e-02,
                -8.54959985e-01,  -2.91046916e-01,  -7.17624159e-01,
                -4.32488571e-01,   3.10453860e-01,  -7.17135445e-01,
                 8.19437699e-01,  -6.49607420e-02,   8.66808786e-01,
                 2.70044097e-01,  -2.74381657e-01,  -2.56179599e+00,
                 5.03296014e-01,  -1.23855471e-01,   5.57114005e-01,
                 6.89388367e-01,   9.49531855e-01,  -4.83667517e-01,
                -6.31565227e-01,   3.70324176e-01,  -3.34280688e+00,
                 5.24436578e-01,  -7.89014569e-01,   1.13592219e-01])

net = Net(['relu','relu','linear'])
net.set_params(pars,shapes)

def get_random_price_deltas(price0, volatility, length, di, depth, former_series = None):
    spread = price0 * volatility
    base = np.random.randn(length)*spread
    frac = Fracdiff([])
    target = frac.re_diff(base,di,depth,former_series)
    return target

def get_random_prices(price0 = 100, volatility = 0.004, jhjj = 10, draft = 0, rng = None):
    spread = price0 * volatility
    res = np.zeros(250+jhjj)
    res[0] = price0
    depth = 0
    if rng is None:
        rng = np.random.randn(250+jhjj)*spread
    for i in range(1,250+jhjj):
        if depth == 0:
            res[i] = res[i-1] + rng[i] + draft
        elif res[i-1] == price0 * 1.1:
            depth += rng[i] + draft
            res[i] = price0 * 1.1
            if depth <= 0:
                res[i] = res[i-1] + depth
                depth = 0
        elif res[i-1] == price0 * 0.9:
            depth += rng[i] + draft
            res[i] = price0 * 0.9
            if depth >= 0:
                res[i] = res[i-1] + depth
                depth = 0
        if res[i] > price0 * 1.1:
            depth = res[i] - price0 * 1.1
            res[i] = price0 * 1.1
        elif res[i] < price0 * 0.9:
            depth = res[i] - price0 * 0.9
            res[i] = price0 * 0.9
    return res[jhjj:]

def draw(record,start,end,vols = None):
    
    p = record[:,-1]
    ema5 = [p[0]*1]
    ema12 = [p[0]*1]
    ema26 = [p[0]*1]
    ema50 = [p[0]*1]
    for i in range(1,len(p)):
        ema5.append(ema5[-1] * 4/6 + p[i] * 2/6)
        ema12.append(ema12[-1] * 11/13 + p[i] * 2/13)
        ema26.append(ema26[-1] * 25/27 + p[i] * 2/27)
        ema50.append(ema50[-1] * 49/51 + p[i] * 2/51)
    ema5 = np.array(ema5)
    ema12 = np.array(ema12)
    ema26 = np.array(ema26)
    ema50 = np.array(ema50)
    
    if vols is not None:
        bottum = 0.05
        left = 0.05
        interval = 0.04
        height = (1 - 2*bottum - interval) * 0.2
        height2 =  (1 - 2*bottum - interval) * 0.8
        width = 1 - 2*left
        plt.figure(figsize = (20,8))
        rect_line1=[left,bottum,width,height]
        rect_line2=[left,bottum+height+interval,width,height2]
        ax = []
        ax.append(plt.axes(rect_line2))
        ax.append(plt.axes(rect_line1))
        candlestick_ohlc(ax[0], record[start:end], width=0.6, colorup='r', colordown='g')
        ax[0].plot(np.array(range(start+1,end+1)),ema5[start:end],'r-')
        ax[0].plot(np.array(range(start+1,end+1)),ema12[start:end],'g-')
        ax[0].plot(np.array(range(start+1,end+1)),ema26[start:end],'b-')
        ax[0].plot(np.array(range(start+1,end+1)),ema50[start:end],'y-')
        ax[0].grid()
        ax[0].set_xlim((start,end+1))
        ax[1].bar(np.array(range(start+1,end+1)),vols[start:end])
        ax[1].set_xlim((start,end+1))
    else:
        fig, ax = plt.subplots(1,1)
        candlestick_ohlc(ax, record[start:end], width=0.6, colorup='r', colordown='g')
        ax.plot(np.array(range(start+1,end+1)),ema5[start:end],'r-')
        ax.plot(np.array(range(start+1,end+1)),ema12[start:end],'g-')
        ax.plot(np.array(range(start+1,end+1)),ema26[start:end],'b-')
        ax.plot(np.array(range(start+1,end+1)),ema50[start:end],'y-')
        ax.grid()
        ax.set_xlim((start,end+1))
    
def get_price(price = 50,num = 500, di = 0.1, di_vol = 0.1, di_draft = 0.001, di_pars = [0.8,0.2]):
    record = []
    sigma = 0.002
    pars = [8.41166428e-01, 1.51552153e-01, 6.01606818e-04, 6.95146183e-06] #000001
    #pars = [  8.18390423e-01, 1.14862833e-01, 2.38844408e-03, 9.19025809e-05] #300024
    #pars = [  8.25494231e-01, 1.47105577e-01, 5.50288111e-04, 3.27392530e-05] #601886
    #pars = [  8.43312325e-01,   1.54637695e-01,   8.57926600e-04,  8.01977836e-06] #000300
    rng = None
    for i in range(num):
        di = di*di_pars[0] + np.random.randn()*di_pars[1]*di_vol + di_draft
        #adjust_sigma
        X = np.column_stack((np.linspace(0.0005,0.006,50)*100,np.repeat(di,50)))
        sigma_loc = np.argmin(np.abs(net.output(X)/100 - sigma))
        sigma_adj = X[sigma_loc,0]/100
        rng = get_random_price_deltas(price,sigma_adj,260,di,100,rng)
        res = get_random_prices(price,sigma_adj,draft = pars[2]/260*price, rng = rng)
        record.append([i+1,res[0],np.max(res),np.min(res),res[-1],(sigma*(1+np.random.randn()*0.01))*1e8*np.log(res[-1]),sigma,di])
        temp = res[-1] / price - 1 - pars[2]
        #realized = (np.std(res[1:] - res[:-1])/price)**2
        base = pars[3] + sigma**2 * 260 * pars[0] + (temp)**2 * pars[1]
        base /= 260
        #base = sigma**2
        #rnd = np.max([np.random.randn()*0.001**2,-0.1*base])
        sigma = np.sqrt(base) 
        price = res[-1]
    record = np.array(record)
    #plt.plot(record[:,-1]*np.sqrt(250))
    return record

if __name__ == '__main__':
    
    import scipy.stats as sts
    from myquant.wyshare import *
    from myquant.figarch import *
    from myquant.arfima import *
    from myquant.garch import *
    
    data = ts.get_tick_data('300024',date = '2016-06-01')
    data = data.set_index('time').sort()
    prices = data['price'].values*1
    
    
#    data = ts.get_hist_data(code = '300024',ktype='5').sort()
#    prices = data['close'].values*1
    prices = np.array(prices)[np.array(range(400))*10]
    ret = prices[1:]/prices[:-1]-1
    frac = Fracdiff(ret)
    frac.train(100)
    frac._acfs(ret,10)
    
    arfima = Arfima(ret,1,100,1)
    arfima.train()
    arfima.get_next()
    arfima.get_param_stats()
    ress = arfima.res
    
    garch = fiGarch(ret,1,1,1,1)
    garch.train()
    di = garch.pars[-3]
    plt.plot(garch.sigma)
    
    temp = get_random_price_deltas(50,0.001,260,0.1,100)
    temp = get_random_price_deltas(50,0.001,260,0.1,100,temp)
    temp = get_random_prices(50,0.004,10,0,temp)
    plt.plot(temp)
    frac = Fracdiff([])
    frac._acfs(temp,10)
    
    
    record = get_price(50,1000)
    draw(record[:,:5],record[:,-3],0,999)
    close = record[:,-4]
    ret = close[1:]/close[:-1]-1
    
    data = get_h_data('000001',index = True,start = '20100101')
    close = data['close'].values
    ret = close[1:]/close[:-1]-1
    
    x = ret
    garch = fiGarch(x,1,1,1,1,100)
    garch.train()
    di = garch.pars[-3]
    plt.plot(garch.sigma)
    
    print(np.sum(np.abs(x-garch.rps)>garch.sigma*1.28)/len(x))
    
    ress = garch.res/garch.sigma
    sts.kstest(ress,'norm')
    
    x2 = garch.res/garch.sigma
    arma = Arfima(x2,1,100,1)
    arma.train()
    ress = arma.res
    
    
    
    ress = garch.res
    num = 14
    Q = len(ress)*(len(ress)+2)*np.sum(frac._acfs(ress,num)**2/(len(ress) - np.array(range(num)) - 1))
    p = 1 - sts.chi2(num).cdf(Q)
    print(p)
    
    frac = Fracdiff(ret)
    frac.train()
    
    arma = Arfima(x,0,100,0)
    arma.train()
    ress = arma.res
    
    record = get_price(50,500)
    draw(record,record[:,-2],0,499)
    close = record[:,-3]
    ret = close[1:]/close[:-1]-1