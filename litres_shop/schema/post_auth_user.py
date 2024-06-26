auth_user = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "integer"
    },
    "error": {
      "type": "null"
    },
    "payload": {
      "type": "object",
      "properties": {
        "data": {
          "type": "object",
          "properties": {
            "sid": {
              "type": "string"
            }
          },
          "required": [
            "sid"
          ]
        }
      },
      "required": [
        "data"
      ]
    }
  },
  "required": [
    "status",
    "error",
    "payload"
  ]
}