export interface Chunk {
  chunk_text: string;
  score: number;
}

export interface SemanticResult {
  filename: string;
  chunks: Chunk[];
}

export {};