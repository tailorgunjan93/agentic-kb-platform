export interface SemanticResult {
  id: string;
  filename: string;
  path: string;
  uploaded_at: string;
}

export interface SearchResponse {
  files: SemanticResult[];
}
