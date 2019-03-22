def hi(cafe):
    if len(cafe) < 5:
        print(cafe)
        cafe += (1,)
        # cafe += '1'
        hi(cafe)
    print('끝')
    print(cafe)
    # for i in range(1):
    #     cafe.append(i)
    #     hi(cafe)

hi((999,))

