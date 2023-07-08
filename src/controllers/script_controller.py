import os
import io
from flask import Blueprint, render_template, abort, send_file, request, jsonify

from src.wb_quotation_summary_excel_script.quotation_summary_excel_script \
    import main as quotation_summary_excel_script

from src.wb_quotation_comparison_excel_script.quotation_comparison_excel_script \
    import main as quotation_comparison_excel_script

from typing import Callable

script_controller = Blueprint('script_controller',
                              __name__)

def process(data_source: dict, exec_script: Callable[[dict], str]) -> str:
    print("data source json", data_source)
    target_path = exec_script(data_source)

    if os.path.isfile(target_path):
        try:
            with open(target_path, "rb") as bytes:
                return send_file(
                    io.BytesIO(bytes.read()),
                    mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            
            os.remove(target_path)
        except Exception as e:
            print("error: ", f"{e}")
            return jsonify(
                success=False,
                errorMessage=f"{e}"
            )


@script_controller.route("/script/quotation_summary_excel", methods=['GET', 'POST'])
def quotation_summary_excel():
    if (request.method == "GET"):
        return jsonify(
            success=True,
            message="This endpoint is working"
        )
    if (request.method == "POST"):
        dataSource: dict = request.get_json()
        return process(dataSource, quotation_summary_excel_script)



@script_controller.route("/script/quotation_comparison_excel_script", methods=['GET', 'POST'])
def quotation_comparison_excel():
    if (request.method == "GET"):
        return jsonify(
            success=True,
            message="This endpoint is working"
        )
    if (request.method == "POST"):
        dataSource: dict = request.get_json()
        return process(dataSource, quotation_comparison_excel_script)
