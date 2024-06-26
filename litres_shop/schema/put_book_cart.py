book_cart = {
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
            "added_art_ids": {
              "type": "array",
              "items": [
                {
                  "type": "integer"
                }
              ]
            },
            "failed_art_ids": {
              "type": "array",
              "items": {}
            }
          },
          "required": [
            "added_art_ids",
            "failed_art_ids"
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