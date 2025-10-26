import React from "react";
import { SemanticResult } from "../types";

const ResultCard: React.FC<{ result: SemanticResult }> = ({ result }) => (
  <div className="border p-4 rounded shadow mb-4">
    <h3 className="font-semibold mb-2">{result.filename}</h3>
    {result.chunks.map((chunk, i) => (
      <div key={i} className="mb-2">
        <p className="text-sm text-gray-700">{chunk.chunk_text}</p>
        <p className="text-xs text-gray-500">Score: {chunk.score.toFixed(3)}</p>
      </div>
    ))}
  </div>
);

export default ResultCard;
