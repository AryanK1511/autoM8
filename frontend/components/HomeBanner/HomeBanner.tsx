'use client';

import React, { useEffect, useState } from 'react';
import { DocsIcon, GitHubIcon, SearchBar } from '@/components';
import { Button } from '@nextui-org/react';
import { useUser } from '@auth0/nextjs-auth0/client';
import Link from 'next/link';

const fetchData = async () => {
  try {
    const response = await fetch('/api/test');

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    const result = await response.json();
    console.log(result);
    return result;
  } catch (error) {
    console.error('Failed to fetch data:', error);
  }
};

// ========== HOME BANNER COMPONENT ==========
export const HomeBanner: React.FC = () => {
  const { user, error, isLoading } = useUser();

  useEffect(() => {
    if (user) {
      fetchData();
    }
  }, [user]);

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
