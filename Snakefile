infile = config["i"]

rule all:
    input:
        f"output/{infile}.reversed.txt"

rule reverse:
    input:
        infile
    output:
        f"output/{infile}.reversed"
    shell:
        """
        tac {input} > {output}
        """