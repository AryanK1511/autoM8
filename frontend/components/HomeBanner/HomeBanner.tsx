import React from 'react';
import { SearchBar } from '@/components';
import { Button } from '@nextui-org/react';

// ========== HOME BANNER COMPONENT ==========
export const HomeBanner: React.FC = () => {
  return (
    <div className="grid grid-cols-1 gap-4">
      <div
        className="flex justify-center text-center mx-auto flex-col w-full"
        style={{
          backgroundImage:
            'linear-gradient(to right, rgba(0, 255, 0, 0.2) 10%, rgba(255, 255, 255, 0) 50%, rgba(0, 255, 0, 0.2) 90%)',
          padding: '2rem',
          borderRadius: '1rem',
        }}
      >
        <div className="flex justify-between w-[400px] text-center mx-auto py-5">
          <span>267 users</span>
          <span>&#x2022;</span>
          <span>MIT License</span>
          <span>&#x2022;</span>
          <span>21 automations</span>
        </div>
        <div>
          <h1 className="text-6xl font-extrabold my-2">Effortless automation</h1>
          <p className="my-4 text-2xl">A platform to run all your automation tasks from the web.</p>
        </div>
        <div>
          <Button color="danger" variant="bordered" startContent={<UserIcon />}>
            Delete user
          </Button>
          <Button color="danger" variant="bordered" startContent={<UserIcon />}>
            Delete user
          </Button>
        </div>
        <div>
          <SearchBar />
        </div>
      </div>
    </div>
  );
};
