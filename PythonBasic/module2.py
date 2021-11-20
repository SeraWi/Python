import module

module.price(3)
module.price_morning(3)
module.price_soldier(3)

# as 별칭
import module as mv

mv.price(3)
mv.price_morning(3)
mv.price_soldier(3)

#바로 함수 호출 가능한 방법
from module import *
price(3)
price_soldier(3)
price_morning(3)

from module import price, price_morning
price(5)
price_morning(6)
#price_soldier(5) 사용 불가

#함수 하나만 import 할때 별칭 설정  ->price 라고 하면
from module import price_soldier as price
price(3)
