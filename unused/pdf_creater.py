from weasyprint.document import DocumentMetadata
from Source.formatter.manga_helper_list import MangaHelperList, MangaHelperEntry
from options import Options
from weasyprint import HTML
from jinja2 import Template
from typing import Optional


def create_search_result(query, options):
    assert "export_folder" in options, "Export folder is not defined"
    export_folder: str = options["export_folder"]
    # Read template file
    with open(constants.SEARCH_HTML_TEMPLATE) as file_:
        template = Template(file_.read())
    # render template with the recipe as argument
    html = template.render(query=query, results=query.get_results())
    target_file: str = export_folder + constants.PREFIX_SEARCH_RESULT_FOLDER + query.get_filename()
    doc = HTML(string=html).render()
    doc.write_pdf(target_file)

def create_manga_helper_list(manga_helper_list: MangaHelperList):
    """Returns the path to the exported pdf"""
    print("Export Recipe: ", manga_helper_list.get_filename())
    # Read template file
    with open(Options.helper_template) as file_:
        template = Template(file_.read())
    # render template with the recipe as argument
    html = template.render(doc=manga_helper_list)

    # Create document Metadata
    meta = DocumentMetadata()
    meta.title = manga_helper_list.title()
    meta.generator = "Kitsune"
    # meta.description = "This file is automatically created with the Gourmet Recipe Manager Exporter.\nFor recipe changes, contact the Builder."
    doc = HTML(string=html).render()
    doc.metadata = meta
    target_file: str = Options.export_path + manga_helper_list.get_file_name()
    doc.write_pdf(target_file)

