from app.domain.models.alira import Alira
from app.presentation.controllers.alira_controller import AliraController

driver = 'Chrome'
image_name_prefix = 'alira_'

alira = Alira(
    url="https://gms-internacional.pre.tecnalis.com/alira-server/login.jsp",
    image_name_prefix=image_name_prefix,
    driver=driver,
    alira_helper=None
)

AC = AliraController()
AS = AC.set_seo_parameters_per_page(alira=alira)

print('------------- termino -----------------')
# print(AS.alira_helper.layouts)
