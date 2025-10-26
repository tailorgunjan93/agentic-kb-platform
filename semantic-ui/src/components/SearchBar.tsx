import React from "react";

interface Props {
  query: string;
  onChange: (val: string) => void;
  onSearch: () => void;
  loading: boolean;
}

const SearchBar: React.FC<Props> = ({ query, onChange, onSearch, loading }) => (
  <div className="flex gap-2 mb-4">
    <input
      type="text"
      value={query}
      onChange={(e) => onChange(e.target.value)}
      placeholder="Ask your KB..."
      className="flex-1 p-2 border rounded"
    />
    <button
      onClick={onSearch}
      disabled={loading}
      className="bg-blue-600 text-white px-4 py-2 rounded"
    >
      {loading ? "Searching..." : "Search"}
    </button>
  </div>
);

export default SearchBar;
