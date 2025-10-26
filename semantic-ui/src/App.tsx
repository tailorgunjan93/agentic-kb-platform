import React, { useState } from "react";
import SearchBar from "./components/SearchBar";
import ResultCard from "./components/ResultCard";
import { searchSemantic } from "./services/searchService";
import { SemanticResult } from "./types";

function App() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<SemanticResult[]>([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    setLoading(true);
    try {
      const data = await searchSemantic(query);
      setResults(data);
    } catch (err) {
      console.error("Search failed", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-6 max-w-3xl mx-auto">
      <SearchBar query={query} onChange={setQuery} onSearch={handleSearch} loading={loading} />
      {results.map((res, idx) => (
        <ResultCard key={idx} result={res} />
      ))}
    </div>
  );
}

export default App;