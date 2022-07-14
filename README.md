# RemoveEmbeddingExecutor

RemoveEmbeddingExecutor deletes the embedding attribute of documents and matches. You can use this to:

* avoid passing embeddings between executors after they're no longer needed
* avoid returning embeddings in API responses

Make sure this executor is placed after any which need embedidngs, e.g. a typical use case would be:

```mermaid
%%{
    init:{
        "theme": "base",
        "themeVariables": {
            "primaryColor": "#fff",
            "primaryBorderColor": "#fff",
            "mainBkg": "#32C8CD",
            "clusterBkg": "#EEEDE78C",
            "secondaryBorderColor": "none",
            "tertiaryBorderColor": "none",
            "lineColor": "#a6d8da"
        }
    }
}%%
     
flowchart LR;
subgraph Encoder;

direction LR;

Encoder/rep-0[""jinahub://YourEncoder""]:::pod;
end;
subgraph Indexer;

direction LR;

Indexer/rep-0[""jinahub://YourIndexer""]:::pod;
end;
subgraph Cleaner;

direction LR;

Cleaner/rep-0[""jinahub://RemoveEmbeddingExecutor""]:::pod;
end;
gatewaystart[gateway]:::GATEWAY --> Encoder:::DEPLOYMENT;
Encoder:::DEPLOYMENT --> Indexer:::DEPLOYMENT;
Indexer:::DEPLOYMENT --> Cleaner:::DEPLOYMENT;
Cleaner:::DEPLOYMENT --> gatewayend[gateway]:::GATEWAY;
classDef INSPECT stroke:#F29C9F
classDef JOIN_INSPECT stroke:#F29C9F
classDef GATEWAY fill:none,color:#000,stroke:none
classDef INSPECT_AUX_PASS stroke-dasharray: 2 2
classDef HEADTAIL fill:#32C8CD1D

classDef EXTERNAL fill:#fff,stroke:#32C8CD
```