import axios from "axios";
import { SemanticResult } from "../types";

export async function searchSemantic(query: string): Promise<SemanticResult[]> {
  const response = await axios.get("/search", { params: { query } });
  return response.data;
}
export {};