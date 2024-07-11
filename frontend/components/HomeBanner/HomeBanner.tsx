import React from 'react';
import { DocsIcon, GitHubIcon, SearchBar } from '@/components';
import { Button } from '@nextui-org/react';
import Link from 'next/link';

// ========== HOME BANNER COMPONENT ==========
export const HomeBanner: React.FC = () => {
  return (
    <div className="grid grid-cols-1 gap-4">
      <div className="flex justify-center text-center mx-auto flex-col w-full">
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
        <div className="py-8">
          <Link href="https://github.com/AryanK1511/autoM8" target="_blank">
            <Button variant="light" className="mx-3" startContent={<GitHubIcon />}>
              GitHub Repository
            </Button>
          </Link>
          <Link href="/" target="_blank">
            <Button variant="light" className="mx-3" startContent={<DocsIcon />}>
              Documentation
            </Button>
          </Link>
        </div>
        <div>
          <SearchBar />
        </div>
      </div>
    </div>
  );
};
