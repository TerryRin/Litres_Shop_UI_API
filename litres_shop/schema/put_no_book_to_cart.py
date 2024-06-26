add_non_existent_book = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "integer"
    },
    "error": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string"
        },
        "title": {
          "type": "string"
        },
        "detail": {
          "type": "string"
        },
        "error_descriptions": {
          "type": "array",
          "items": [
            {
              "type": "object",
              "properties": {
                "loc": {
                  "type": "array",
                  "items": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "string"
                    },
                    {
                      "type": "string"
                    }
                  ]
                },
                "msg": {
                  "type": "string"
                },
                "type": {
                  "type": "string"
                }
              },
              "required": [
                "loc",
                "msg",
                "type"
              ]
            }
          ]
        }
      },
      "required": [
        "type",
        "title",
        "detail",
        "error_descriptions"
      ]
    }
  },
  "required": [
    "status",
    "error"
  ]
}