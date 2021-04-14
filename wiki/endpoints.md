## endpoints

#### Estados

```
GET - api/estados?page_number=intr&page_size=Str
(ordenados de acuerdo a d_estado, default de 32 por página / pagina 1)

  response:
    {
      "data": Array[Estado],
      "pagintation_info": PaginationInfo,
    }

POST - api/estado
  response: 
    {
      "estado": Estado
    }

```

#### Municipios

```
GET - api/municipios?page_number=intr&page_size=Str
(ordenados de acuerdo a D_mnpio, default de 20 por página/ pagina 1)

  response:
    {
      "data": Array[Municipio],
      "pagintation_info": PaginationInfo,
    }
    
POST - api/municipios
  response:
    {
      "municipio": Municipio
    }

```

#### Asentamientos

```
GET - api/asentamientos?page_number=intr&page_size=Str
(ordenados de acuerdo a id_asenta_cpcons, default de 20 por página/ pagina 1)

  response:
    {
      "data": Array[Asentamiento],
      "pagintation_info": PaginationInfo,
    }
    
GET - api/asentamientos/<str:codigo_postal>?page_number=intr&page_size=Str
(ordenados de acuerdo a id_asenta_cpcons, default de 20 por página/ pagina 1)

  response:
    {
      "data": Array[Asentamiento],
      "pagintation_info": PaginationInfo,
    }
    
POST - api/municipios
  response:
    {
      "asentamiento": Asentamiento
    }

```

#### Codigos Postales

```
GET - api/codigos_postales?page_number=intr&page_size=Str
(ordenados de acuerdo a uuid, default de 20 por página/ pagina 1)

  response:
    {
      "data": Array[CodigoPostal],
      "pagintation_info": PaginationInfo,
    }
    
POST - api/municipios
  response:
    {
      "codigo": CodigoPostal
    }
