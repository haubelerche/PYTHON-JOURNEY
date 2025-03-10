def convert(m):
    #accept input, return :) to 🙂
    m1=m.replace(":)","🙂")
    #accept input, return :( to 🙁
    m2=m1.replace(":(","🙁")
    # return str
    return m2

def main():
    # prompt input
    m = str(input())
    #call convert
    res = convert(m)
    # print res
    print(res)
    #call main at bottom

main()



