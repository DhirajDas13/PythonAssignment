# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 13:07:30 2019

@author: DH319684
"""

import xml.sax

class BookHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self.title = ""
      self.author = ""
      self.year = ""
      self.price = ""

   # Call when an element starts
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      if tag == "book":
         print ("*****Book*****")
         category = attributes["category"]
         print ("Category:", category)

   # Call when an elements ends
   def endElement(self, tag):
      if self.CurrentData == "title":
         print ("Title:", self.title)
      elif self.CurrentData == "author":
         print ("Author:", self.author)
      elif self.CurrentData == "year":
         print ("Year:", self.year)
      elif self.CurrentData == "price":
         print ("Price:", self.price)
      self.CurrentData = ""

   # Call when a character is read
   def characters(self, content):
      if self.CurrentData == "title":
         self.title = content
      elif self.CurrentData == "author":
         self.author = content
      elif self.CurrentData == "year":
         self.year = content
      elif self.CurrentData == "price":
         self.price = content
  
if ( __name__ == "__main__"):
   
   # create an XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # override the default ContextHandler
   Handler = BookHandler()
   parser.setContentHandler( Handler )
   
   parser.parse("Books.xml")