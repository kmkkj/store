'''
完成衣服销售数据的统计和分析
需求：
1.1计算总销售额
1.2计算平均每日销售数量
1.3 计算每个种类月销售量占比
衣服：
日期、服饰名称、价格/件、库存数量、销售量/每日
'''
print("---------衣服销售数据的统计和分析--------")
print("日期  服饰名称  价格/件  库存数量  销售量/每日")
print("1号   羽绒服    253.6    500       10")
print("2号   牛仔裤    86.3     600       60")
print("3号    风衣     96.8     335       43")
print("4号    皮草     135.9    855       63")
print("5号    T恤      65.8     632       63")
print("6号    衬衫     49.3     562       120")
print("7号   牛仔裤    86.3     600       72")
print("8号   羽绒服    253.6    500       69")
print("9号   牛仔裤    86.3     600       35")
print("10号   羽绒服    253.6    500      140")
print("11号   牛仔裤    86.3     600      90")
print("12号    皮草     135.9    855      24")
print("13号    T恤      65.8     632      45")
print("14号    风衣     96.8     335      25")
print("15号   牛仔裤    86.3     600       60")
print("16号    T恤      65.8     632      129")
print("17号   羽绒服    253.6    500       10")
print("18号    风衣     96.8     335       43")
print("19号    T恤      65.8     632      63")
print("20号   牛仔裤    86.3     600       60")
print("21号    皮草     135.9    855       63")
print("22号    风衣     96.8     335       60")
print("23号    T恤      65.8     632       58")
print("24号   牛仔裤    86.3     600       140")
print("25号    T恤      65.8     632       48")
print("26号    风衣     96.8     335       43")
print("27号    皮草     135.9    855       57")
print("28号   羽绒服    253.6    500       10")
print("29号    T恤      65.8     632      63")
print("30号    风衣     96.8     335       78")
money=(253.6*(10+69+140+10+10)+86.3*(60+72+35+90+60+60+140)+96.8*(43+25+43+60+43+78)+135.9*(63+24+63+57)+65.8*(63+45+129+63+58+48+63)+49.3*120)
number=((10*3+60*4+43*3+63*5+120+72+69+35+140*2+90+24+45+25+129+58+48+57+78)/30)
proportion1=((10*3+69+140)/(10*3+60*4+43*3+63*5+120+72+69+35+140*2+90+24+45+25+129+58+48+57+78))
proportion2=((60*3+72+35+90+140)/(10*3+60*4+43*3+63*5+120+72+69+35+140*2+90+24+45+25+129+58+48+57+78))
proportion3=((43*3+25+60+78)/(10*3+60*4+43*3+63*5+120+72+69+35+140*2+90+24+45+25+129+58+48+57+78))
proportion4=((63*2+24+57)/(10*3+60*4+43*3+63*5+120+72+69+35+140*2+90+24+45+25+129+58+48+57+78))
proportion5=((63*3+45+129+58+48)/(10*3+60*4+43*3+63*5+120+72+69+35+140*2+90+24+45+25+129+58+48+57+78))
proportion6=(120/(10*3+60*4+43*3+63*5+120+72+69+35+140*2+90+24+45+25+129+58+48+57+78))
print("总销售额为：",money)
print("平均每日销售数量为：",number)
print("羽绒服月销售量占比为：",proportion1)
print("牛仔裤月销售量占比为：",proportion2)
print("风衣月销售量占比为：",proportion3)
print("皮草月销售量占比为：",proportion4)
print("T恤月销售量占比为：",proportion5)
print("衬衫月销售量占比为：",proportion6)

