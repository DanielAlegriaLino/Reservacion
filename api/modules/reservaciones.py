import supabase #pip install supabase
import datetime


supabase_url = 'https://qtqxhfsvnoutethbjwgx.supabase.co'
supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InF0cXhoZnN2bm91dGV0aGJqd2d4Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcwMDYwODYzOCwiZXhwIjoyMDE2MTg0NjM4fQ.Q_6D-my0PC1aneF6NndWynBw7TFsuk0e3rtG7lJgsvQ'
client = supabase.create_client(supabase_url, supabase_key)
fecha = datetime.datetime.now()
fecha_str = fecha.strftime("%Y-%m-%d")

def GenerarReservacion(fecha): #Necesita Recibir la fecha en formato de string/JSON
    response = client.table('ReservacionesEnProceso').insert({"fecha": fecha}).execute()
    id_created = client.table('ReservacionesEnProceso').select('id').eq('fecha', fecha).execute()
    return id_created.data[0]['id']
    
def EstablecerReservacion(fecha, mesa, id_reservacion_proceso):
    response = client.table('ReservacionesEnProceso').select('id').eq('id', id_reservacion_proceso).execute()
    if response.data == []:
        return "False"
    else:
        delete = client.table('ReservacionesEnProceso').delete().eq('id', id_reservacion_proceso).execute()
        response = client.table('ReservacionesRealizadas').insert({"fecha": fecha, "mesa": mesa, "hash": 'gawefawawf'}).execute() ####### El hash generado no es real
        return "True"
    
def BorrarReservacionEstablecida(hash):
    response = client.table('ReservacionesRealizadas').select('hash').eq('hash', hash).execute()
    print(response)
    if response.data == []:
        return False
    else:
        delete = client.table('ReservacionesRealizadas').delete().eq('hash', hash).execute()
        return True

def BorrarReservacionTemporal(id):
    response = client.table('ReservacionesEnProceso').select('id').eq('id', id).execute()
    print(response.data)
    if response.data == []:
        return False
    else:
        delete = client.table('ReservacionesEnProceso').delete().eq('id', id).execute()
        return True

def RevisarMesas(fecha):
    cont = 0
    response = client.table('ReservacionesRealizadas').select('mesa').eq('fecha', fecha).execute()
    usage = client.table('ReservacionesEnProceso').select('id').eq('fecha', fecha).execute()
    print(usage)
    if(usage.data):return [True]*5
    
    res= [False]*5
    if(response.data == []): 
        return res
    print(response.data)
    for i in range(len(response.data)):
        index = response.data[i]['mesa']
        res[index]=True
        
        
        
    return res
            
def getReservas():
    response = client.table('ReservacionesRealizadas').select('fecha').execute()
    return response



    

