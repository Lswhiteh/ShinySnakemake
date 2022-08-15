import shlex
import subprocess
from shiny import App, render, ui, reactive

app_ui = ui.page_fluid(
    ui.input_text("input_file", "Path to input file", "tester.txt"),
    ui.input_text("logfile", "Logfile", "log.txt"),
    ui.input_action_button("run_btn", "Run Pipeline"),
)


def server(input, output, session):
    @output
    @render.text
    @reactive.event(input.run_btn)
    def run_snkmk(): 
        print("foo")
        cmd = f"""snakemake -c 1 --config -i={input.input_file()}"""
        process = subprocess.Popen(shlex.split(cmd), shell=False, stdout=process.PIPE)
        
        with open(input.logfile(), "w") as lfile:
            while True:
                output = process.stdout.readline()
                if process.poll() is not None:
                    break
                if output:
                    print(output.strip())
                    lfile.write(output.strip() + "\n")

        rc = process.poll()


app = App(app_ui, server)
