# Truck Registry Service

## Usage

The responses have the form of

```json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

Subsequent response definitions will only detail the expected value of the `data field`

### List all trucks

**Definitions**

`GET /trucks`

**Responses**

- `200 OK` for success

```json
[
    {
        "identifier": "truck-id-A12345",
        "name": "Truck A",
        "truck_type": "electric",
        "controller_gateway": "192.1.68.0.2"
    },
    {
        "identifier": "truck-id-B12345",
        "name": "Truck B",
        "truck_type": "hybrid",
        "controller_gateway": "192.1.68.0.9"
    }
]
```
### Registering a new truck

**Definitions**

`POST /trucks`

**Arguments**

- `"identifier":string` a globally unique identifier for this truck
- `"name":string` a friendly name for this truck
- `"truck_typ":string` the type of the truck as understood by the client
- `"controller_gateway":string` the IP address of the truck's controller

If a truck with the given identifier already exists, the existing truck will be overwritten.

**Response**

- `201 Created` on success

```json
{
    "identifier": "truck-id-A12345",
    "name": "Truck A",
    "truck_type": "electric",
    "controller_gateway": "192.1.68.0.2"
}
```

## Lookup truck details

**Definition**

`GET /truck/<identifier>`

**Response**

- `404 Not Found` if the truck does not exist
- `200 OK` on success

```json
{
    "identifier": "truck-id-A12345",
    "name": "Truck A",
    "truck_type": "electric",
    "controller_gateway": "192.1.68.0.2"
}
```

## Delete a truck

**Definition**

`DELETE /trucks/<identifier>`

**Response**

- `404 Not Found` if the truck does not exist
- `204 No Content` on success