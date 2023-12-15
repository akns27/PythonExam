class country:
  def __init__(self, name, population, capital):
    self.name = name
    self.population = population
    self.capital = capital
  def show(self):
    print("""
          국가의 이름은 {}입니다.
          국가의 인구는 {}입니다.
          국가의 수도는 {}입니다.
          """.format(self.name,self.population,self.capital))

country1 = country(name = '캐나다', population='3825만 이상', capital='오타와')
country2 = country(name='대한민국', population='5000만 이상', capital='서울')

country1.show()
country2.show()
