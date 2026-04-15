import os, requests, json

from qgis.core import *
from .compat import FIELD_STRING, FIELD_DOUBLE, FIELD_BOOL
BIKE_PNG_PATH = os.path.join(os.path.dirname(__file__),  "bike.png")


#ステーション情報を表示
def create_gbfs_free_bike_layer(self,url):
    
    #ステーション情報取得
    response = requests.get(url)
    text = response.text
    data = json.loads(text)
    
    #free_bike情報保持
    gbfs_free_bike = data["data"]["bikes"]
    #self.stations_info = gbfs_free_bike
    
    #create qgisVectorLayer
    layer = QgsVectorLayer("Point", self.system_name + "_free_bike", "memory")
    
    # Start of the edition 
    layer.startEditing()
    
    #カラムを作成        
    layer.dataProvider().addAttributes( [
        QgsField('bike_id'               , FIELD_STRING), 
        QgsField('is_reserved'           , FIELD_BOOL), 
        QgsField('is_disabled'           , FIELD_BOOL), 
        QgsField('vehicle_type_id'       , FIELD_STRING), 
        QgsField('last_reported'         , FIELD_STRING), 
        QgsField('current_range_meters'  , FIELD_STRING), 
        QgsField('current_fuel_percent'  , FIELD_STRING), 
        QgsField('station_id'            , FIELD_STRING), 
        QgsField('home_station_id'       , FIELD_STRING), 
        QgsField('pricing_plan_id'       , FIELD_STRING), 
        QgsField('vehicle_equipment'     , FIELD_STRING), 
        QgsField('available_until'       , FIELD_STRING),
        QgsField('android'               , FIELD_STRING), 
        QgsField('ios '                  , FIELD_STRING), 
        QgsField('web'                   , FIELD_STRING),  
        QgsField('lon'                   , FIELD_DOUBLE), 
        QgsField('lat'                   , FIELD_DOUBLE) 
        ] )
    
    
    #update
    layer.updateFields()
    
    # Addition of features
    for bike in gbfs_free_bike:
        f = QgsFeature()
        f.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(bike["lon"],bike["lat"])))
        
        feature = []
        
        feature.append(bike['bike_id'              ] if 'bike_id'              in bike else None)
        feature.append(bike['is_reserved'          ] if 'is_reserved'          in bike else None)
        feature.append(bike['is_disabled'          ] if 'is_disabled'          in bike else None)
        feature.append(bike['vehicle_type_id'      ] if 'vehicle_type_id'      in bike else None)
        feature.append(bike['last_reported'        ] if 'last_reported'        in bike else None)
        feature.append(bike['current_range_meters' ] if 'current_range_meters' in bike else None)
        feature.append(bike['current_fuel_percent' ] if 'current_fuel_percent' in bike else None)
        feature.append(bike['station_id'           ] if 'station_id'           in bike else None)
        feature.append(bike['home_station_id'      ] if 'home_station_id'      in bike else None)
        feature.append(bike['pricing_plan_id'      ] if 'pricing_plan_id'      in bike else None)
        feature.append(bike['vehicle_equipment'    ] if 'vehicle_equipment'    in bike else None)
        feature.append(bike['available_until'      ] if 'available_until'      in bike else None)
        feature.append(bike['android'              ] if 'android'              in bike else None)
        feature.append(bike['ios '                 ] if 'ios '                 in bike else None)
        feature.append(bike['web'                  ] if 'web'                  in bike else None)
        feature.append(bike['lon'                  ] if 'lon'                  in bike else None)
        feature.append(bike['lat'                  ] if 'lat'                  in bike else None)
       
        f.setAttributes(feature)
        layer.addFeature(f)            
    
    # saving changes and adding the layer
    layer.updateExtents() 
    
    #set layer symbol
    symbol = QgsRasterMarkerSymbolLayer(BIKE_PNG_PATH)
    symbol.setSize(5)
    layer.renderer().symbol().changeSymbolLayer(0, symbol )
    
    layer.commitChanges()
    QgsProject.instance().addMapLayer(layer)

#ステーション情報を表示(jp-style)
def create_gbfs_free_bike_layer_jp(self,url):

    
    #ステーション情報取得
    response = requests.get(url)
    text = response.text
    data = json.loads(text)
    
    #free_bike情報保持
    gbfs_free_bike = data["data"]["bikes"]
    #self.stations_info = gbfs_free_bike
    
    #create qgisVectorLayer
    layer = QgsVectorLayer("Point", self.system_name + "_free_bike", "memory")
    
    # Start of the edition 
    layer.startEditing()
    
    #カラムを作成        
    layer.dataProvider().addAttributes( [
        QgsField('車両ID'                     , FIELD_STRING), 
        QgsField('予約状況（True:予約中）'    , FIELD_BOOL), 
        QgsField('車両利用可否(True:利用不可)', FIELD_BOOL), 
        QgsField('車種ID'                     , FIELD_STRING), 
        QgsField('ステータス最終取得時間'     , FIELD_STRING), 
        QgsField('残走行可能距離(m)'          , FIELD_STRING), 
        QgsField('残燃料(%)'                  , FIELD_STRING), 
        QgsField('ステーションID'             , FIELD_STRING), 
        QgsField('ホームステーションID'       , FIELD_STRING), 
        QgsField('料金プランID'               , FIELD_STRING), 
        QgsField('車両装備'                   , FIELD_STRING), 
        QgsField('車両返却期限'               , FIELD_STRING),
        QgsField('android'                    , FIELD_STRING), 
        QgsField('ios '                       , FIELD_STRING), 
        QgsField('web'                        , FIELD_STRING),  
        QgsField('lon'                        , FIELD_DOUBLE), 
        QgsField('lat'                        , FIELD_DOUBLE) 
        ] )
    
    
    #update
    layer.updateFields()
    
    # Addition of features
    for bike in gbfs_free_bike:
        f = QgsFeature()
        f.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(bike["lon"],bike["lat"])))
        
        feature = []
        
        feature.append(bike['bike_id'              ] if 'bike_id'              in bike else None)
        feature.append(bike['is_reserved'          ] if 'is_reserved'          in bike else None)
        feature.append(bike['is_disabled'          ] if 'is_disabled'          in bike else None)
        feature.append(bike['vehicle_type_id'      ] if 'vehicle_type_id'      in bike else None)
        feature.append(bike['last_reported'        ] if 'last_reported'        in bike else None)
        feature.append(bike['current_range_meters' ] if 'current_range_meters' in bike else None)
        feature.append(bike['current_fuel_percent' ] if 'current_fuel_percent' in bike else None)
        feature.append(bike['station_id'           ] if 'station_id'           in bike else None)
        feature.append(bike['home_station_id'      ] if 'home_station_id'      in bike else None)
        feature.append(bike['pricing_plan_id'      ] if 'pricing_plan_id'      in bike else None)
        feature.append(bike['vehicle_equipment'    ] if 'vehicle_equipment'    in bike else None)
        feature.append(bike['available_until'      ] if 'available_until'      in bike else None)
        feature.append(bike['android'              ] if 'android'              in bike else None)
        feature.append(bike['ios '                 ] if 'ios '                 in bike else None)
        feature.append(bike['web'                  ] if 'web'                  in bike else None)
        feature.append(bike['lon'                  ] if 'lon'                  in bike else None)
        feature.append(bike['lat'                  ] if 'lat'                  in bike else None)
       
        f.setAttributes(feature)
        layer.addFeature(f)            
    
    # saving changes and adding the layer
    layer.updateExtents() 
    
    #set layer symbol
    symbol = QgsRasterMarkerSymbolLayer(BIKE_PNG_PATH)
    symbol.setSize(5)
    layer.renderer().symbol().changeSymbolLayer(0, symbol )
    
    layer.commitChanges()
    QgsProject.instance().addMapLayer(layer)
        