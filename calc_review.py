starting_capital = 10000.00
cash = 8144.66

adbe_entry = 247.03; adbe_shares = 4; adbe_cost = 988.10; adbe_current = 248.50; adbe_stop = 185.00; adbe_fv = 311.70
now_entry = 89.47; now_shares = 2; now_cost = 178.94; now_current = 100.82; now_stop = 58.00; now_fv = 121.45
intu_entry = 445.00; intu_shares = 0.67; intu_cost = 299.39; intu_current = 321.50; intu_stop = 348.00; intu_fv = 595.00
googl_entry = 388.91; googl_shares = 1; googl_cost = 388.91; googl_current = 387.81; googl_stop = 310.00; googl_fv = 414.00

adbe_mkt = adbe_shares * adbe_current
now_mkt = now_shares * now_current
intu_mkt = intu_shares * intu_current
googl_mkt = googl_shares * googl_current

adbe_pnl = adbe_mkt - adbe_cost
now_pnl = now_mkt - now_cost
intu_pnl = intu_mkt - intu_cost
googl_pnl = googl_mkt - googl_cost

adbe_ret = (adbe_current - adbe_entry) / adbe_entry * 100
now_ret = (now_current - now_entry) / now_entry * 100
intu_ret = (intu_current - intu_entry) / intu_entry * 100
googl_ret = (googl_current - googl_entry) / googl_entry * 100

adbe_stopdist = (adbe_current - adbe_stop) / adbe_stop * 100
now_stopdist = (now_current - now_stop) / now_stop * 100
intu_stopdist = (intu_current - intu_stop) / intu_stop * 100
googl_stopdist = (googl_current - googl_stop) / googl_stop * 100

adbe_mos = (adbe_fv - adbe_current) / adbe_current * 100
now_mos = (now_fv - now_current) / now_current * 100
intu_mos = (intu_fv - intu_current) / intu_current * 100
googl_mos = (googl_fv - googl_current) / googl_current * 100

total_mkt = adbe_mkt + now_mkt + intu_mkt + googl_mkt
total_value = cash + total_mkt
port_return = (total_value - starting_capital) / starting_capital * 100

print("ADBE: mkt=" + str(round(adbe_mkt,2)) + " pnl=" + str(round(adbe_pnl,2)) + " ret=" + str(round(adbe_ret,2)) + "% stopdist=" + str(round(adbe_stopdist,1)) + "% mos=" + str(round(adbe_mos,1)) + "% wt=" + str(round(adbe_mkt/total_value*100,2)) + "%")
print("NOW:  mkt=" + str(round(now_mkt,2)) + " pnl=" + str(round(now_pnl,2)) + " ret=" + str(round(now_ret,2)) + "% stopdist=" + str(round(now_stopdist,1)) + "% mos=" + str(round(now_mos,1)) + "% wt=" + str(round(now_mkt/total_value*100,2)) + "%")
print("INTU: mkt=" + str(round(intu_mkt,2)) + " pnl=" + str(round(intu_pnl,2)) + " ret=" + str(round(intu_ret,2)) + "% stopdist=" + str(round(intu_stopdist,1)) + "% mos=" + str(round(intu_mos,1)) + "% wt=" + str(round(intu_mkt/total_value*100,2)) + "%")
print("INTU STOP BREACH: " + str(intu_current) + " vs stop " + str(intu_stop) + " = " + str(round(intu_stopdist,1)) + "% AUTO-SELL")
print("GOOGL:mkt=" + str(round(googl_mkt,2)) + " pnl=" + str(round(googl_pnl,2)) + " ret=" + str(round(googl_ret,2)) + "% stopdist=" + str(round(googl_stopdist,1)) + "% mos=" + str(round(googl_mos,1)) + "% wt=" + str(round(googl_mkt/total_value*100,2)) + "%")
print("TOTAL: mkt=" + str(round(total_mkt,2)) + " total_val=" + str(round(total_value,2)) + " port_ret=" + str(round(port_return,2)) + "%")
print("cash=" + str(cash) + " cash_pct=" + str(round(cash/total_value*100,1)) + "%")

cash2 = cash + intu_mkt
tv2 = cash2 + adbe_mkt + now_mkt + googl_mkt
ret2 = (tv2 - starting_capital) / starting_capital * 100
print("--- POST INTU SELL ---")
print("cash2=" + str(round(cash2,2)) + " total_val2=" + str(round(tv2,2)) + " port_ret2=" + str(round(ret2,2)) + "%")
print("ADBE wt=" + str(round(adbe_mkt/tv2*100,2)) + "% NOW wt=" + str(round(now_mkt/tv2*100,2)) + "% GOOGL wt=" + str(round(googl_mkt/tv2*100,2)) + "% cash_pct=" + str(round(cash2/tv2*100,2)) + "%")
print("INTU realized pnl=" + str(round(intu_pnl,2)) + " return=" + str(round(intu_ret,2)) + "%")
