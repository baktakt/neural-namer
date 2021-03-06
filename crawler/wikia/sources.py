"""List of Wikia sources to scape."""

SOURCES = [
    {
        "author": "Tolkien",
        "dump_url": "http://s3.amazonaws.com/wikia_xml_dumps/l/lo/lotr_pages_current.xml.7z",
        "root": "/n:mediawiki/n:page",
        "xpath": "./n:title/text()",
        "where": {
            "xpath": "./n:revision/n:text/text()",
            "contains": r'''\{\{Infobox Person'''
        },
        "ignore": [r"^.+:", r"\(.+\)$"]
    },
    {
        "author": "George Martin",
        "dump_url": "http://s3.amazonaws.com/wikia_xml_dumps/g/ga/gameofthrones_pages_current.xml.7z",
        "root": "/n:mediawiki/n:page",
        "xpath": "./n:title/text()",
        "where": {
            "xpath": "./n:revision/n:text/text()",
            "contains": r'''\{\{Character'''
        },
        "ignore": [r"^.+:", r"\(.+\)$"]
    },
    {
        "author": "Robert Jordan",
        "dump_url": "http://s3.amazonaws.com/wikia_xml_dumps/w/wo/wot_pages_current.xml.7z",
        "root": "/n:mediawiki/n:page",
        "xpath": "./n:title/text()",
        "where": {
            "xpath": "./n:revision/n:text/text()",
            "contains": r'''\{\{ character'''
        },
        "ignore": [r"^.+:", r"\(.+\)$"]
    },
    {
        "author": "Steven Erikson",
        "dump_url": "http://s3.amazonaws.com/wikia_xml_dumps/m/ma/malazan_pages_current.xml.7z",
        "root": "/n:mediawiki/n:page",
        "xpath": "./n:title/text()",
        "where": {
            "xpath": "./n:revision/n:text/text()",
            "contains": r'''\[\[Category:(Males|Females)'''
        },
        "ignore": [r"^.+:", r"\(.+\)$"]
    },
    {
        "author": "Brian Jacques",
        "dump_url": "http://s3.amazonaws.com/wikia_xml_dumps/r/re/redwall_pages_current.xml.7z",
        "root": "/n:mediawiki/n:page",
        "xpath": "./n:title/text()",
        "where": {
            "xpath": "./n:revision/n:text/text()",
            "contains": r'''\{\{Character\|'''
        },
        "ignore": [r"^.+:", r"\(.+\)$"]
    },
    {
        "author": "Frank Herbert",
        "dump_url": "http://s3.amazonaws.com/wikia_xml_dumps/d/du/dune_pages_current.xml.7z",
        "root": "/n:mediawiki/n:page",
        "xpath": "./n:title/text()",
        "where": {
            "xpath": "./n:revision/n:text/text()",
            "contains": r'''\[\[Category:(Males|Females)'''
        },
        "ignore": [r"^.+:", r"\(.+\)$"]
    }
]
