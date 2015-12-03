from powerPlay import generateTemplate

template = generateTemplate("Infosys_Template.pptx", "My Analysis.pptx")
output = template.generate_template_from_source_ppt()

print("{} is genareted as template".format(output))
