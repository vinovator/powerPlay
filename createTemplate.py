# Python 2.76
# createTemplate.py

"""
This program calls the  powerplay library I created based on Python-pptx library
Create a template based on an existing powerpoint file
Template will be a copy of the source and adds a slide for each layout present in source
TO:DO - Find way to delete slides from source so that template is a bare skeleton
Added issue #186 to scanny/python-pptx repository
"""

from powerPlay import generateTemplate

template = generateTemplate("Infosys_Template.pptx", "My Analysis.pptx")
output = template.generate_template_from_source_ppt()

print("{} is genareted as template".format(output))
