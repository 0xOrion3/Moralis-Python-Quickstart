import json
from moralis import evm_api

api_key = "YOUR_API_KEY"

params = {
    "address": "0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB", 
    "token_id": "3931", 
    "chain": "eth", 
    "format": "decimal", 
    "normalizeMetadata": True, 
}

result = evm_api.nft.get_nft_metadata(
    api_key=api_key,
    params=params,
)

print(json.dumps(result, indent=4))

# result
"""
{
    "token_address": "0xb47e3cd837ddf8e4c57f05d70ab865de6e193bbb",
    "token_id": "3931",
    "amount": "1",
    "owner_of": "0x1cf2b8c64aed32bff2ae80e701681316d3212afd",
    "token_hash": "3c86855c82470edd82df190019e83f16",
    "block_number_minted": "5754322",
    "block_number": "13868997",
    "transfer_index": [
        13868997,
        30,
        36,
        0
    ],
    "contract_type": null,
    "name": "CRYPTOPUNKS",
    "symbol": "\u03fe",
    "token_uri": "https://www.larvalabs.com/cryptopunks/details/3931",
    "metadata": "{\"image\":\"https://www.larvalabs.com/cryptopunks/cryptopunk3931.webp\",\"name\":\"CryptoPunk 3931\",\"attributes\":[\"Vampire Hair\",\"Goat\"],\"description\":\"Male\"}",
    "last_token_uri_sync": null,
    "last_metadata_sync": "2022-05-12T18:00:22.340Z",
    "minter_address": "0xc352b534e8b987e036a93539fd6897f53488e56a",
    "normalized_metadata": {
        "name": "CryptoPunk 3931",
        "description": "Male",
        "animation_url": null,
        "external_link": null,
        "image": "https://www.larvalabs.com/cryptopunks/cryptopunk3931.webp",
        "attributes": [
            {
                "trait_type": "type",
                "value": "Male",
                "display_type": null,
                "max_value": null,
                "trait_count": 0,
                "order": null
            },
            {
                "trait_type": "attribute",
                "value": "Vampire Hair",
                "display_type": null,
                "max_value": null,
                "trait_count": 0,
                "order": null
            },
            {
                "trait_type": "attribute",
                "value": "Goat",
                "display_type": null,
                "max_value": null,
                "trait_count": 0,
                "order": null
            }
        ]
    }
}
"""