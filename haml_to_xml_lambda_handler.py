import boto3
import os
import sys
from ihiw_converter import Converter


s3 = boto3.client('s3')


def lambda_handler(event, context):
    try:
        bucket = event['s3']['bucket']

        csvFileObject = event['s3']['Keycsv']
    
        manufacturer = event['s3']['Keymanufacturer']

        xmlFileObject = event['s3']['Keyxml']

        converter = Converter(csvFileObject,manufacturer,xmlFileObject)
        Manufacturer,Table = converter.DetermineManufacturer()
        
        if Manufacturer == 'OneLambda':
            print('Manufacturer', Manufacturer)
            converter.ProcessOneLambda(Table)
        elif Manufacturer == 'Immucor':
            print('Manufacturer', Manufacturer)
            converter.ProcessImmucor(Table)
        else: 
            print('Not known manufacturer, unable to convert file')
            
    except ValueError: 
        print('Not known manufacturer, unable to convert file')