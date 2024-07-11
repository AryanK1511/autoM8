import React from 'react';
import { Input } from '@nextui-org/input';
import { SearchIcon } from './SearchIcon';

// ========== SEARCH BAR COMPONENT ==========
export const SearchBar: React.FC = () => {
  return (
    <div>
      <Input type="text" placeholder="Search autoM8" endContent={<SearchIcon />} />
    </div>
  );
};
