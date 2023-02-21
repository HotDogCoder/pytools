from core.config import constants
from app.application.repositories_interfaces.alira_repository_interface import AliraRepositoryInterface
from app.domain.models.alira import Alira
from core.util.path.path_helper import PathHelper
from core.util.whatsapp.whatsapp_helper import WhatsappHelper


class AliraRepository(AliraRepositoryInterface):

    def __init__(self):
        super().__init__()

    def set_seo_parameters_per_page(self, alira: Alira):

        url = constants.API_UPLOAD_SCREENSHOT
        multiple_files = []
        path_helper = PathHelper()
        # path = alira.alira_helper.trace_helper.write_to_qa_report_pdf_log()
        path = f'{path_helper.get_project_root_path()}/storage/exportations/qa_report_log/qa_report_log_{alira.alira_helper.trace_helper.now}.txt'
        whatsapp_helper = WhatsappHelper(number='51966153268@c.us')
        files = whatsapp_helper.update_file(paths=[path], mime='application/pdf')
        for file in files:
            whatsapp_helper.send_message("", photo=file)
        whatsapp_helper.send_message("Reporte de QA", photo="")

        return alira

    def set_seo_redirection(self, alira: Alira):
        return alira

    def get_layouts(self, alira: Alira):
        return alira

    def set_page_url(self, alira: Alira):
        return alira