import xmltodict 


def xml_to_dict(xml_string):
    dictionary = xmltodict.parse(xml_string)
    return dictionary


# Example usage
xml_string = '''
<root>
    <person>
        <name>John Doe</name>
        <age>30</age>
        <city>New York</city>
    </person>
    <person>
        <name>Jane Smith</name>
        <age>25</age>
        <city>London</city>
    </person>
</root>
'''

converted_dict = xml_to_dict(xml_string)
print(converted_dict)
