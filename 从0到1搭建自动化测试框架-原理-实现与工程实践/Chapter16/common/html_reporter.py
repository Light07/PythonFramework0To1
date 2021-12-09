import time

import os
import traceback

from common.my_logger import MyLogger
from configs.global_config import get_config

my_logger = MyLogger().get_logger(__name__)


# used to map all the test cases
def format_time(time_delta: float):
    ms = "{0:0.3f}".format(time_delta % 1000).split('.')[-1]
    seconds = "{0:0>2d}".format(int(time_delta % 60))
    minutes = "{0:0>2d}".format(int(time_delta / 60))
    hours = "{0:0>2d}".format(int(time_delta / (60 * 60)))
    return hours + "h: " + minutes + "m: " + seconds + "s: " + ms + "ms"


def generate_html_report(output_folder, passed_cases, failed_cases, error_cases, skipped_cases, start_time,
                         platform_info,
                         auto_refresh):
    with open(output_folder + os.sep + "report.html", "w") as report_file_handler:
        back_ground_color_page = "#FFFFFF"
        bg_color_column = "#ADADAD"
        end_time = time.time()
        execution_time = format_time(end_time - start_time)

        css = """
        <style type="text/css">
            a:link,a:visited{
                text-decoration:none;
            }
            a:hover{
                text-decoration:underline;
                background-color:#8E8E8E;
            }
        </style>
        """

        # java script code for filter function
        java_script_code_for_filter = """
        <script type="text/javascript">

            function changeTag(){
                var my_select = document.getElementById("testcase_tag");
                if (my_select.value == "ALL"){
                    //all_failed_test_cases is  represent for all failed test cases
                    if(document.getElementById("all_failed_test_cases")){
                        all_failed_test_case = document.getElementById("all_failed_test_cases");
                        all_failed_test_case.style.display="none";
                        all_failed_test_case.style.display="block";

                        all_failed_case_list = document.getElementsByClassName("all_failed_case");
                        for(var i=0;i<all_failed_case_list.length;i++){
                            all_failed_case_list[i].style.display="block";
                        }
                        document.getElementById("num_fail").innerHTML=i;
                    }
                    
                    if(document.getElementById("all_error_test_cases")){
                            all_error_test_cases = document.getElementById("all_error_test_cases");
                            all_error_test_cases.style.display="none";
                            all_error_test_cases.style.display="block";
    
                            all_error_case_list = document.getElementsByClassName("all_error_case");
                            for(var i=0;i<all_error_case_list.length;i++){
                                all_error_case_list[i].style.display="block";
                            }
                            document.getElementById("num_error").innerHTML=i;
                        }
                    
                    if(document.getElementById("all_skipped_test_cases")){
                            all_skipped_test_cases = document.getElementById("all_skipped_test_cases");
                            all_skipped_test_cases.style.display="none";
                            all_skipped_test_cases.style.display="block";
    
                            all_skipped_case_list = document.getElementsByClassName("all_skipped_case");
                            for(var i=0;i<all_skipped_case_list.length;i++){
                                all_skipped_case_list[i].style.display="block";
                            }
                            document.getElementById("num_skip").innerHTML=i;
                        }   
                    
                    //all_passed_test_cases is  represent for all passed test cases
                    if (document.getElementById("all_passed_test_cases")){
                        all_passed_test_case = document.getElementById("all_passed_test_cases");
                        all_passed_test_case.style.display="none";
                        all_passed_test_case.style.display="block";
                        all_passed_case_list = document.getElementsByClassName("all_passed_case");

                        for(var j=0;j<all_passed_case_list.length;j++){
                            all_passed_case_list[j].style.display="block";
                        }
                        document.getElementById("num_pass").innerHTML=j;
                    }
                }

                var l = new Array()
                k = 0;
                all_failed_case_list = document.getElementsByClassName("all_failed_case");

                for(var i=0;i<all_failed_case_list.length;i++){
                    all_failed_case_list[i].style.display="none";

                    if (all_failed_case_list[i].getAttribute("name").indexOf(my_select.value) != -1){
                        l[k] = all_failed_case_list[i];
                        k = k + 1;
                    }
                }
                
                all_error_case_list = document.getElementsByClassName("all_error_case");
                
                for(var i=0;i<all_error_case_list.length;i++){
                    all_error_case_list[i].style.display="none";
        
                    if (all_error_case_list[i].getAttribute("name").indexOf(my_select.value) != -1){
                        l[k] = all_error_case_list[i];
                        k = k + 1;
                    }
                }

                all_passed_case_list = document.getElementsByClassName("all_passed_case");

                for(var i=0;i<all_passed_case_list.length;i++){
                    all_passed_case_list[i].style.display="none";
                    if (all_passed_case_list[i].getAttribute("name").indexOf(my_select.value) != -1){
                        l[k] = all_passed_case_list[i];
                        k = k + 1;
                    }
                }

                all_skipped_case_list = document.getElementsByClassName("all_skipped_case");

                for(var i=0;i<all_skipped_case_list.length;i++){
                    all_skipped_case_list[i].style.display="none";
                    if (all_skipped_case_list[i].getAttribute("name").indexOf(my_select.value) != -1){
                        l[k] = all_skipped_case_list[i];
                        k = k + 1;
                    }
                }

                if (document.getElementById("all_failed_test_cases")){
                    all_failed_test_case = document.getElementById("all_failed_test_cases");
                    all_failed_test_case.style.display="none";
                    all_failed_test_case.style.display="block";
                }

                if (document.getElementById("all_error_test_cases")){
                    all_error_test_case = document.getElementById("all_error_test_cases");
                    all_error_test_case.style.display="none";
                    all_error_test_case.style.display="block";
                }

                if (document.getElementById("all_passed_test_cases")){
                    all_passed_test_case = document.getElementById("all_passed_test_cases");
                    all_passed_test_case.style.display="none";
                    all_passed_test_case.style.display="block";
                }

                if (document.getElementById("all_skipped_test_cases")){
                    all_skipped_test_case = document.getElementById("all_skipped_test_cases");
                    all_skipped_test_case.style.display="none";
                    all_skipped_test_case.style.display="block";
                }
                num_failed_case = 0;
                num_error_case = 0;
                num_passed_case = 0;
                num_skipped_case = 0;

                for(var i=0;i<l.length;i++){
                    l[i].style.display="block";
                    if ("all_failed_case"==l[i].className){
                        num_failed_case = num_failed_case + 1;
                    }
                    if ("all_error_case"==l[i].className){
                        num_error_case = num_error_case + 1;
                    }
                    if ("all_passed_case"==l[i].className){
                        num_passed_case = num_passed_case + 1;
                    }
                    if ("all_skipped_case"==l[i].className){
                        num_skipped_case = num_skipped_case + 1;
                    }
                }

                if (document.getElementById("num_fail")){
                    document.getElementById("num_fail").innerHTML=num_failed_case;
                }
                if (document.getElementById("num_error")){
                    document.getElementById("num_error").innerHTML=num_error_case;
                }
                if (document.getElementById("num_pass")){
                    document.getElementById("num_pass").innerHTML=num_passed_case;
                }
                if (document.getElementById("num_skip")){
                    document.getElementById("num_skip").innerHTML=num_skipped_case;
                }
            }

        </script>
        """

        java_script_copy_failed_testcases = """
        <script>
            function copyFailedTestCase(){
                document.getElementById("failed_testcase_names").style.display="none";
                if (%s === 1){
                    document.getElementById("copy_status_info").innerHTML = "<font color=red>Copied 1 TestCase</font>";
                } else if(%s > 1){
                    document.getElementById("copy_status_info").innerHTML = "<font color=red>Copied %s TestCases</font>";
                }
                setTimeout(function(){
                    document.getElementById("copy_status_info").innerHTML = "";
                    document.getElementById("failed_testcase_names").style.display="block";
                }, 2000);
            }
        </script>
        """ % (len(failed_cases), len(failed_cases), len(failed_cases))

        refresh_string = "<meta http-equiv=\"Refresh\" content=\"25\" />"

        str_high_chart = """
        <html>
            <head>%s
                <title>Automation Test Report</title>
                %s
                %s
                %s
            </head>
            <script type="text/javascript" src="http://cdn.hcharts.cn/jquery/jquery-1.8.3.min.js"></script>
            <script type="text/javascript" src="http://cdn.hcharts.cn/highcharts/highcharts.js"></script>
            <script type="text/javascript" src="http://cdn.hcharts.cn/highcharts/highcharts-3d.js"></script>
            <script type="text/javascript" src="https://cdn.jsdelivr.net/clipboard.js/1.5.12/clipboard.min.js"></script>
            <script>
                $(function () {
                    $('#chart_div').highcharts({
                        chart: {
                            type: 'pie',
                            options3d: {
                                enabled: true,
                                alpha: 50,
                                beta: 0
                            }
                        },
                        credits: {
                            enabled: false
                        },
                        colors:[
                            '#478608',
                            '#760202',
                            '#FF0303'
                          ],
                        title: {
                            text: 'Automation Test Report'
                        },
                        tooltip: {
                            pointFormat: '{series.name}: <b>{point.percentage:.1f}%%</b>'
                        },
                        plotOptions: {
                            pie: {
                                size:'100%%',
                                allowPointSelect: true,
                                cursor: 'pointer',
                                depth: 30,
                                dataLabels: {
                                    enabled: true,
                                    formatter: function(){
                                        return this.point.name+"-"+this.percentage.toFixed(1)+"%%";
                                    }
                                }
                            }
                        },
                        series: [{
                            type: 'pie',
                            name: 'Testcase Result',
                            data: [
                                ['Passed',   %s],
                                ['Failed',   %s],
                                ['RunError', %s]
                            ]
                        }]
                    });
                });
              </script>
        """ % (
            refresh_string if auto_refresh else "",
            css,
            java_script_code_for_filter,
            java_script_copy_failed_testcases,
            len(passed_cases),
            len(failed_cases),
            len(error_cases)
        )

        report_file_handler.write(str_high_chart)
        # 从全局变量中获取environment
        environment = get_config('config')["env"]

        str_top_table = """
        <body  bgcolor='%s'>
        <table align='center' cellpadding=0 cellspacing=0 style='border-collapse: collapse' width='925'>
            <tr>
                <td>
                    <div id='chart_div' style="min-width: 500px; height: 300px; margin: 0 auto"></div>
                </td>
                <td>
                    <table border='1' align='center' cellpadding=0 cellspacing=0 style='border-collapse: collapse' width='400'>
                        <tr  bgcolor='%s'>
                            <td>
                                <font color='blue'>Report Generate Time</font>
                            </td>
                            <td width='150' align='center'>
                                <font color='blue'>%s</font>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <font color='blue'>Total Execution Time</font>
                            </td>
                            <td width='150' align='center'><font color='blue'>%s</font>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <font color='blue'>Total TestCases</font>
                            </td>
                            <td align='center' width='150'>
                                <font color='blue'>%s</font>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <font color='blue'>TestCases Passed</font>
                            </td>
                            <td align='center'>
                                <font color='blue'>%s</font>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <font color='blue'>TestCases Failed</font>
                            </td>
                            <td align='center'>
                                <font color='blue'>%s</font>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <font color='blue'>TestCases Run Error</font>
                            </td>
                            <td align='center'>
                                <font color='blue'>%s</font>
                            </td>
                        </tr>
                        
                        <tr>
                            <td>
                                <font color='blue'>Environment</font>
                            </td>
                            <td align='center'>
                                <font color='blue'>%s</font>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <font color='blue'>Platform</font>
                            </td>
                            <td align='center'>
                                <font color='blue'>%s</font>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <font color='blue'>AutomationFramework</font>
                            </td>
                            <td align='center'>
                            <font color='blue'>请关注微信公众号 - iTesting</font>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
        <br>
        """ % (
            back_ground_color_page,
            bg_color_column,
            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
            execution_time,
            len(passed_cases) + len(failed_cases),
            len(passed_cases),
            len(failed_cases),
            len(error_cases),
            environment,
            platform_info
        )

        report_file_handler.write(str_top_table)
        all_testcases = passed_cases + failed_cases + error_cases + skipped_cases

        # generate the drop down list for all the different tags
        html_drop_down_list = """
        <table border='0' align='center' cellpadding=0 cellspacing=0 style='border-collapse: collapse' width='925'>
            <tr>
                <td width='200'>Filter TestCases By Package: </td>
                <td>
        """
        report_file_handler.write(html_drop_down_list)

        all_testcases_package_list = passed_cases + failed_cases + error_cases + skipped_cases

        report_file_handler.write("<select id=\"testcase_tag\" onchange=\"changeTag()\">")
        filter_class = []
        for testcase in all_testcases_package_list:
            filter_class.append('ALL' + '.' + testcase["class_name"])

        report_file_handler.write("<option value='ALL'>")
        report_file_handler.write("ALL")
        report_file_handler.write("</option>")
        for item in set(filter_class):
            report_file_handler.write("<option value='%s'>" % item)
            report_file_handler.write("%s" % item[4:])
            report_file_handler.write("</option>")
        report_file_handler.write("</select>")
        report_file_handler.write("</td><td align='left'><p id='copy_status_info'></p></td><td>")

        if len(failed_cases) > 0:
            str_failed_testcase_names = ""

            for failed_testcase in failed_cases:
                str_failed_testcase_names += failed_testcase["testcase"] + " "

            str_failed_testcases = """
            <div align="center">
                <button id="failed_testcase_names" class='failed_testcase_names' data-clipboard-text="%s" onclick="copyFailedTestCase()">
                    Click Me to Copy the Failed TestCase Names to Clipboard!
                </button>
            </div>
            <script>
                new Clipboard('.failed_testcase_names');
            </script>
            """ % str_failed_testcase_names

            report_file_handler.write(str_failed_testcases)

        report_file_handler.write("</td></tr></table>")
        report_file_handler.write("<br>")

        if len(failed_cases) > 0:
            failed_testcase_table = """
            <table border='1' align='center' cellpadding=0 cellspacing=0 style='border-collapse: collapse' width='925'>
                <tr id='all_failed_test_cases' bgcolor='%s' width='925'>
                    <td width='125' align='center'>
                        <b>
                            <font color='red'>TestCaseID</font>
                        </b>
                    </td>
                    <td width='650' style='word-break:break-all' align='center'>
                        <b>
                            <font id='num_fail' color='red'>%s Test %s Failed</font>
                        </b>
                    </td>
                    <td width='150' align='center'>
                        <b>
                            <font color='red'>Execution Time</font>
                        </b>
                    </td>
                </tr>
            """ % (
                bg_color_column,
                len(failed_cases),
                "Cases" if len(failed_cases) > 1 else "Case"
            )

            report_file_handler.write(failed_testcase_table)

            for failed_testcase in failed_cases:
                module_name = failed_testcase["running_testcase_name"]
                module_name_display = failed_testcase["testcase"]
                report_file_handler.write(
                    "<tr class='all_failed_case' name=ALL.%s  width='925'>" % failed_testcase["testcase"])

                report_file_handler.write(
                    "<td width='125' align='center' style='word-break:break-all;no-wrap:no-wrap'>")
                report_file_handler.write(
                    "<a title='Click to go to test center' href='https://testcenter.englishtown.com/testlink/linkto.php?tprojectPrefix=ET&item=testcase&id=ET-%s'><font color='red'>" %
                    failed_testcase["testcase_id"])
                report_file_handler.write("%s" % failed_testcase["testcase_id"])
                report_file_handler.write("</font></a>")
                report_file_handler.write("</td>")

                testcase_information = """
                    <td width='650'style='word-break:break-all'>
                    <a  href='%s'>
                        <font color='blue'>
                            %s
                        </font>
                    </a>
                    """ % (
                    module_name,
                    module_name_display
                )

                report_file_handler.write(testcase_information)

                report_file_handler.write(
                    " <a title='%s'> (" % 'Please see the execution logs for more details' + failed_testcase[
                        "exception_type"] + ") </a>")

                try:
                    report_file_handler.write(
                        "<a title='Log' href='%s'>        <font color='#F18428'>   Log</font> </a>" %
                        list(failed_testcase["log_list"])[0])
                except BaseException:
                    my_logger.error(traceback.format_exc())

                try:
                    if failed_testcase["screenshot_list"]:
                        report_file_handler.write(
                            "<a title='Screenshot' href='%s'> <font color='#F18428'> - Screenshot</font> </a>" %
                            list(failed_testcase["screenshot_list"])[0])
                except BaseException:
                    my_logger.error(traceback.format_exc())

                try:
                    if len(list(failed_testcase["log_list"])) > 1:
                        report_file_handler.write(
                            "<a title='ReRun_Log' href='%s'> <font color='#F18428'> | ReRun_Log</font> </a>" %
                            list(failed_testcase["log_list"])[1])
                except BaseException:
                    my_logger.error(traceback.format_exc())

                try:

                    if len(list(failed_testcase["screenshot_list"])) > 1:
                        report_file_handler.write(
                            "<a title='ReRun_Screenshot' href='%s'> <font color='#F18428'> - ReRun_Screenshot</font> </a>" %
                            list(failed_testcase["screenshot_list"])[1])
                except BaseException:
                    my_logger.error(traceback.format_exc())

                report_file_handler.write("</td>")

                report_file_handler.write("<td width='150' align='center' >")
                report_file_handler.write("<font color='red'>")
                report_file_handler.write("%s" % failed_testcase["execution_time"])
                report_file_handler.write("</font>")
                report_file_handler.write("</td></tr>")
            report_file_handler.write("</table>")
        report_file_handler.write("<br>")

        if len(error_cases) > 0:
            error_testcase_table = """
            <table border='1' align='center' cellpadding=0 cellspacing=0 style='border-collapse: collapse' width='925'>
                <tr id='all_error_test_cases' bgcolor='%s' width='925'>
                    <td width='125' align='center'>
                        <b>
                            <font color='red'>TestCaseID</font>
                        </b>
                    </td>
                    <td width='650' style='word-break:break-all' align='center'>
                        <b>
                            <font id='num_error' color='red'>%s Test %s encountered error during run</font>
                        </b>
                    </td>
                    <td width='150' align='center'>
                        <b>
                            <font color='red'>Execution Time</font>
                        </b>
                    </td>
                </tr>
            """ % (
                bg_color_column,
                len(error_cases),
                "Cases" if len(list(error_cases)) > 1 else "Case"
            )

            report_file_handler.write(error_testcase_table)

            for error_testcase in error_cases:
                module_name = error_testcase["running_testcase_name"]
                module_name_display = error_testcase["testcase"]
                report_file_handler.write(
                    "<tr class='all_error_case' name=ALL.%s  width='925'>" % error_testcase["testcase"])

                report_file_handler.write(
                    "<td width='125' align='center' style='word-break:break-all;no-wrap:no-wrap'>")
                report_file_handler.write(
                    "<a title='Click to go to test center' href='https://testcenter.xxxx.com/testlink/linkto.php?tprojectPrefix=ET&item=testcase&id=ET-%s'><font color='red'>" %
                    error_testcase["testcase_id"])
                report_file_handler.write("%s" % error_testcase["testcase_id"])
                report_file_handler.write("</font></a>")
                report_file_handler.write("</td>")

                testcase_information = """
                    <td width='650'style='word-break:break-all'>
                    <a  href='%s'>
                        <font color='blue'>
                            %s
                        </font>
                    </a>
                    """ % (
                    module_name,
                    module_name_display
                )

                report_file_handler.write(testcase_information)

                report_file_handler.write(
                    " <a title='%s'> (" % 'Please see the execution logs for more details' + error_testcase[
                        "exception_type"] + ") </a>")

                try:
                    report_file_handler.write(
                        "<a title='Log' href='%s'>        <font color='#F18428'>   Log</font> </a>" %
                        list(error_testcase["log_list"])[0])
                except BaseException:
                    my_logger.error(traceback.format_exc())

                try:
                    if error_testcase["screenshot_list"]:
                        report_file_handler.write(
                            "<a title='Screenshot' href='%s'> <font color='#F18428'> - Screenshot</font> </a>" %
                            list(error_testcase["screenshot_list"])[0])
                except BaseException:
                    my_logger.error(traceback.format_exc())

                try:
                    if len(list(error_testcase["log_list"])) > 1:
                        report_file_handler.write(
                            "<a title='ReRun_Log' href='%s'> <font color='#F18428'> | ReRun_Log</font> </a>" %
                            list(error_testcase["log_list"])[1])
                except BaseException:
                    my_logger.error(traceback.format_exc())

                try:

                    if len(list(error_testcase["screenshot_list"])) > 1:
                        report_file_handler.write(
                            "<a title='ReRun_Screenshot' href='%s'> <font color='#F18428'> - ReRun_Screenshot</font> </a>" %
                            list(error_testcase["screenshot_list"])[1])
                except BaseException:
                    my_logger.error(traceback.format_exc())

                report_file_handler.write("</td>")

                report_file_handler.write("<td width='150' align='center' >")
                report_file_handler.write("<font color='red'>")
                report_file_handler.write("%s" % error_testcase["execution_time"])
                report_file_handler.write("</font>")
                report_file_handler.write("</td></tr>")
            report_file_handler.write("</table>")
        report_file_handler.write("<br>")

        if len(passed_cases) > 0:
            passed_testcase_table = """
            <table border='1' align='center' cellpadding=0 cellspacing=0 style='border-collapse: collapse' width='925'>
                <tr id='all_passed_test_cases' bgcolor='%s' width='925'>
                    <td width='125' align='center'>
                        <b>
                            <font color='blue'>TestCaseID</font>
                        </b>
                    </td>
                    <td width='650' style='word-break:break-all' align='center'>
                        <b>
                            <font id='num_pass' color='blue'>%s  Test %s Passed</font>
                        </b>
                    </td>
                    <td width='150' align='center'>
                        <b>
                            <font color='blue'>Execution Time</font>
                        </b>
                    </td>
                </tr>
            """ % (
                bg_color_column,
                len(passed_cases),
                "Cases" if len(list(passed_cases)) > 1 else "Case"
            )
            report_file_handler.write(passed_testcase_table)

            for passed_testcase in passed_cases:
                module_name = passed_testcase["running_testcase_name"]
                module_name_display = passed_testcase['testcase']

                report_file_handler.write(
                    "<tr class='all_passed_case' name=ALL.%s  width='925'>" % passed_testcase["testcase"])

                report_file_handler.write("<td width='125' align='center' >")
                report_file_handler.write(
                    "<a title='Click to go to test center' href='https://testcenter.xxxx.com/testlink/linkto.php?tprojectPrefix=ET&item=testcase&id=ET-%s'> <font color='blue'>" %
                    passed_testcase["testcase_id"])
                report_file_handler.write("%s" % passed_testcase["testcase_id"])
                report_file_handler.write("</font></a>")
                report_file_handler.write("</td>")

                report_file_handler.write("<td width='650' style='word-break:break-all'>")
                report_file_handler.write("<a title='Click to see the log & screenshot' href='")
                report_file_handler.write(module_name)
                report_file_handler.write(
                    "'><font color='%s'>" % (
                        "blue" if passed_testcase["re_run"] == 0 else "green"))
                report_file_handler.write(module_name_display)

                # show re-run got passed in report
                if passed_testcase["re_run"] == 1:
                    report_file_handler.write("<font color='chocolate'> -- Re-Run Passed</font>")

                if passed_testcase in error_cases:
                    report_file_handler.write("<font color='orange'> -- Miss Attribute</font>")

                report_file_handler.write("</font>")
                report_file_handler.write("</font></a>")

                report_file_handler.write("</td>")

                report_file_handler.write("<td width='150' align='center'>")
                report_file_handler.write("<font color='blue'>")

                report_file_handler.write("%s" % passed_testcase["execution_time"])
                report_file_handler.write("</font>")
                report_file_handler.write("</td></tr>")
            report_file_handler.write("</table>")
        report_file_handler.write("<br>")

        if len(skipped_cases) > 0:
            skipped_testcase_table = """
            <table border='1' align='center' cellpadding=0 cellspacing=0 style='border-collapse: collapse' width='925'>
                <tr id='all_skipped_test_cases' bgcolor='%s' width='925'>
                    <td width='125' align='center'>
                        <b>
                            <font color='gray'>TestCaseID</font>
                        </b>
                    </td>
                    <td width='650' style='word-break:break-all' align='center'>
                        <b>
                            <font id='num_skip' color='gray'>%s  Test %s Skipped</font>
                        </b>
                    </td>
                    <td width='150' align='center'>
                        <b>
                            <font color='gray'>Execution Time</font>
                        </b>
                    </td>
                </tr>
            """ % (
                bg_color_column,
                len(skipped_cases),
                "Cases" if len(list(skipped_cases)) > 1 else "Case"
            )
            report_file_handler.write(skipped_testcase_table)

            for skipped_testcase in skipped_cases:
                module_name = skipped_testcase["running_testcase_name"]
                module_name_display = skipped_testcase['testcase']

                report_file_handler.write(
                    "<tr class='all_skipped_case' name=ALL.%s  width='925'>" % skipped_testcase["testcase"])

                report_file_handler.write("<td width='125' align='center' >")
                report_file_handler.write(
                    "<a title='Click to go to test center' href='https://testcenter.xxxx.com/testlink/linkto.php?tprojectPrefix=ET&item=testcase&id=ET-%s'> <font color='gray'>" %
                    skipped_testcase["testcase_id"])
                report_file_handler.write("%s" % skipped_testcase["testcase_id"])
                report_file_handler.write("</font></a>")
                report_file_handler.write("</td>")

                report_file_handler.write("<td width='650' style='word-break:break-all'>")
                report_file_handler.write("<a title='Click to see the log & screenshot' href='")
                report_file_handler.write(module_name if module_name else "None")
                report_file_handler.write(
                    "'><font color='%s'>" % (
                        "gray"))
                report_file_handler.write(module_name_display)

                # show re-run got passed in report
                if skipped_testcase["re_run"] == 1:
                    report_file_handler.write("<font color='chocolate'> -- Re-Run Passed</font>")

                if skipped_testcase in error_cases:
                    report_file_handler.write("<font color='orange'> -- Miss Attribute</font>")

                report_file_handler.write("</font>")
                report_file_handler.write("</font></a>")

                report_file_handler.write("</td>")

                report_file_handler.write("<td width='150' align='center'>")
                report_file_handler.write("<font color='gray'>")

                report_file_handler.write("%s" % skipped_testcase["execution_time"])
                report_file_handler.write("</font>")
                report_file_handler.write("</td></tr>")
            report_file_handler.write("</table>")
        report_file_handler.write("<br>")

        report_file_handler.write("<br><br>")
        report_file_handler.write("</body></html>")
