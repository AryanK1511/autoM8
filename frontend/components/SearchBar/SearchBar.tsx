'use client';

import React from 'react';
import { Input } from '@nextui-org/input';
import { SearchIcon } from '@/components';

// ========== SEARCH BAR COMPONENT ==========
export const SearchBar: React.FC = () => {
  // Handle Form Submission
  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    console.log('Hello');
  };

  return (
    <div className="flex items-center justify-center p-4">
      <form onSubmit={handleSubmit} className="flex items-center space-x-2 w-[600px]">
        <Input
          variant="bordered"
          type="text"
          placeholder="Search autoM8"
          classNames={{
            input: 'py-3 px-4 rounded-l-md rounded-r-none text-md font-semibold',
            label: 'sr-only',
            inputWrapper: [
              'shadow-lg shadow-indigo-600',
              'py-6',
              'backdrop-blur-xl',
              'backdrop-saturate-200s',
              'group-data-[focus=true]:bg-default-200/50',
            ],
          }}
          endContent={<SearchIcon />}
        />
        <button
          type="submit"
          className="py-3 px-4 bg-indigo-600 text-white rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500"
        >
          <span className="text-md font-semibold">Search</span>
        </button>
      </form>
    </div>
  );
};
