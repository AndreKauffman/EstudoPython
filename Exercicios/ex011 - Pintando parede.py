heigth = float(input("altura da parede: "))
width = float(input("largura da parede: "))
area = heigth*width
ink = area / 2
print("sua parede tem a dimensão de {}X{} e sua área é de {}.\nPara pintar sua parede, você precisará de {}Ls de tinta".format(heigth, width, area, ink))
