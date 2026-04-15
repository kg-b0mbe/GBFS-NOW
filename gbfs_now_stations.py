import os, requests, json

from qgis.core import *
from .compat import FIELD_STRING, FIELD_INT, FIELD_DOUBLE, FIELD_BOOL
STATION_PNG_PATH = os.path.join(os.path.dirname(__file__),  "station.png")


#ステーション情報を表示
def create_gbfs_station_layer(self,url):
    
    #ステーション情報取得
    response = requests.get(url)
    text = response.text
    data = json.loads(text)
    
    #station情報保持
    gbfs_stations = data["data"]["stations"]
    self.stations_info = gbfs_stations
    
    #create qgisVectorLayer
    layer = QgsVectorLayer("Point", self.system_name + "_stations", "memory")
    
    # Start of the edition 
    layer.startEditing()
    
    #カラムを作成        
    layer.dataProvider().addAttributes( [
        QgsField('station_id'            , FIELD_STRING), 
        QgsField('name'                  , FIELD_STRING), 
        QgsField('short_name'            , FIELD_STRING), 
        QgsField('capacity'              , FIELD_INT), 
        QgsField('address'               , FIELD_STRING), 
        QgsField('cross_street'          , FIELD_STRING), 
        QgsField('region_id'             , FIELD_STRING), 
        QgsField('post_code'             , FIELD_STRING), 
        QgsField('rental_methods'        , FIELD_STRING), 
        QgsField('is_virtual_station'    , FIELD_BOOL),   
        #QgsField('station_area'          , FIELD_STRING), 
        QgsField('parking_type'          , FIELD_STRING), 
        QgsField('parking_hoop'          , FIELD_BOOL),   
        QgsField('contact_phone '        , FIELD_STRING), 
        #QgsField('vehicle_capacity'      , FIELD_STRING), 
        QgsField('vehicle_type_capacity' , FIELD_STRING), 
        QgsField('is_valet_station'      , FIELD_BOOL),   
        QgsField('is_charging_station'   , FIELD_BOOL), 
        QgsField('android'               , FIELD_STRING), 
        QgsField('ios '                  , FIELD_STRING), 
        QgsField('web'                   , FIELD_STRING),  
        QgsField('lon'                   , FIELD_DOUBLE), 
        QgsField('lat'                   , FIELD_DOUBLE) 
        ] )
    
    
    #update
    layer.updateFields()
    
    # Addition of features
    for station in gbfs_stations:
        f = QgsFeature()
        f.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(station["lon"],station["lat"])))
        
        feature = []
        
        feature.append(station['station_id'           ] if 'station_id'            in station else None)
        feature.append(station['name'                 ] if 'name'                  in station else None)
        feature.append(station['short_name'           ] if 'short_name'            in station else None)
        feature.append(station['capacity'             ] if 'capacity'              in station else None)
        feature.append(station['address'              ] if 'address'               in station else None)
        feature.append(station['cross_street'         ] if 'cross_street'          in station else None)
        feature.append(station['region_id'            ] if 'region_id'             in station else None)
        feature.append(station['post_code'            ] if 'post_code'             in station else None)
        feature.append(", ".join(station['rental_methods']) if 'rental_methods'    in station else None)
        feature.append(station['is_virtual_station'   ] if 'is_virtual_station'    in station else None)
        #feature.append(station['station_area'         ] if 'station_area'          in station else None)
        feature.append(station['parking_type'         ] if 'parking_type'          in station else None)
        feature.append(station['parking_hoop'         ] if 'parking_hoop'          in station else None)
        feature.append(station['contact_phone '       ] if 'contact_phone '        in station else None)
        #feature.append(station['vehicle_capacity'     ] if 'vehicle_capacity'      in station else None)
        feature.append('\n'.join([f"{key}: {value}" for key, value in station['vehicle_type_capacity'].items()]) if 'vehicle_type_capacity' in station else None)
        feature.append(station['is_valet_station'     ] if 'is_valet_station'      in station else None)
        feature.append(station['is_charging_station'  ] if 'is_charging_station'   in station else None)
        feature.append(station['android'              ] if 'android'               in station else None)
        feature.append(station['ios '                 ] if 'ios '                  in station else None)
        feature.append(station['web'                  ] if 'web'                   in station else None)
        feature.append(station['lon'                  ] if 'lon'                   in station else None)
        feature.append(station['lat'                  ] if 'lat'                   in station else None)
        
        f.setAttributes(feature)
        layer.addFeature(f)            
    
    # saving changes and adding the layer
    layer.updateExtents() 
    
    #set layer symbol
    symbol = QgsRasterMarkerSymbolLayer(STATION_PNG_PATH)
    symbol.setSize(5)
    layer.renderer().symbol().changeSymbolLayer(0, symbol )
    
    layer.commitChanges()
    QgsProject.instance().addMapLayer(layer)

#ステーション情報を表示(jp-style)
def create_gbfs_station_layer_jp(self,url):

    #ステーション情報取得
    response = requests.get(url)
    text = response.text
    data = json.loads(text)
    
    #station情報保持
    gbfs_stations = data["data"]["stations"]
    self.stations_info = gbfs_stations
    
    #create qgisVectorLayer
    layer = QgsVectorLayer("Point", self.system_name + "_stations", "memory")
    
    # Start of the edition 
    layer.startEditing()
    
    #カラムを作成        
    layer.dataProvider().addAttributes( [
        QgsField('ステーションID'            , FIELD_STRING), 
        QgsField('ステーション名'                  , FIELD_STRING), 
        QgsField('ステーション名_略称'            , FIELD_STRING), 
        QgsField('最大駐輪可能台数（ラック数）'              , FIELD_STRING),
        QgsField('住所'               , FIELD_STRING), 
        QgsField('道路・交差点名称'          , FIELD_STRING), 
        QgsField('リージョンID'             , FIELD_STRING), 
        QgsField('郵便番号'             , FIELD_STRING), 
        QgsField('決済方法'        , FIELD_STRING),   
        QgsField('仮想ステーションフラグ'    , FIELD_BOOL), 
        #QgsField('仮想ステーション領域'          , FIELD_STRING), 
        QgsField('駐輪場種別'          , FIELD_STRING), 
        QgsField('駐輪フープフラグ'          , FIELD_BOOL), 
        QgsField('電話番号'        , FIELD_STRING),  
        #QgsField('vehicle_capacity'      , FIELD_STRING), 
        QgsField('vehicle_type_capacity' , FIELD_STRING), 
        QgsField('係員フラグ'      , FIELD_STRING), 
        QgsField('チャージャーステーションフラグ'   , FIELD_BOOL), 
        QgsField('android-uri'               , FIELD_STRING), 
        QgsField('ios-uri'                  , FIELD_STRING), 
        QgsField('web-uri'                   , FIELD_STRING),
        QgsField('lon'                   , FIELD_DOUBLE), 
        QgsField('lat'                   , FIELD_DOUBLE) 
        ] )
    
    
    #update
    layer.updateFields()
    
    # Addition of features
    for station in gbfs_stations:
        f = QgsFeature()
        f.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(station["lon"],station["lat"])))
        
        feature = []
        
        feature.append(station['station_id'           ] if 'station_id'            in station else None)
        feature.append(station['name'                 ] if 'name'                  in station else None)
        feature.append(station['short_name'           ] if 'short_name'            in station else None)
        feature.append(station['capacity'             ] if 'capacity'              in station else None)
        feature.append(station['address'              ] if 'address'               in station else None)
        feature.append(station['cross_street'         ] if 'cross_street'          in station else None)
        feature.append(station['region_id'            ] if 'region_id'             in station else None)
        feature.append(station['post_code'            ] if 'post_code'             in station else None)
        feature.append(", ".join(station['rental_methods']) if 'rental_methods'    in station else None)
        feature.append(station['is_virtual_station'   ] if 'is_virtual_station'    in station else None)
        #feature.append(station['station_area'         ] if 'station_area'          in station else None)
        feature.append(station['parking_type'         ] if 'parking_type'          in station else None)
        feature.append(station['parking_hoop'         ] if 'parking_hoop'          in station else None)
        feature.append(station['contact_phone '       ] if 'contact_phone '        in station else None)
        #feature.append(station['vehicle_capacity'     ] if 'vehicle_capacity'      in station else None)
        feature.append('\n'.join([f"{key}: {value}" for key, value in station['vehicle_type_capacity'].items()]) if 'vehicle_type_capacity' in station else None)
        feature.append(station['is_valet_station'     ] if 'is_valet_station'      in station else None)
        feature.append(station['is_charging_station'  ] if 'is_charging_station'   in station else None)
        feature.append(station['android'              ] if 'android'               in station else None)
        feature.append(station['ios '                 ] if 'ios '                  in station else None)
        feature.append(station['web'                  ] if 'web'                   in station else None)
        feature.append(station['lon'                  ] if 'lon'                   in station else None)
        feature.append(station['lat'                  ] if 'lat'                   in station else None)
        
        f.setAttributes(feature)
        layer.addFeature(f)            
    
    # saving changes and adding the layer
    layer.updateExtents() 
    
    #set layer symbol
    symbol = QgsRasterMarkerSymbolLayer(STATION_PNG_PATH)
    symbol.setSize(5)
    layer.renderer().symbol().changeSymbolLayer(0, symbol )

    layer.commitChanges()
    QgsProject.instance().addMapLayer(layer)
        