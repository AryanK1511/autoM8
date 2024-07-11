'use client';

import React from 'react';
import { Avatar } from '@nextui-org/react';
import { useUser } from '@auth0/nextjs-auth0/client';
import { ExploreIcon, LogoutIcon, ProfileIcon, SaveIcon } from '../Icon';
import { Dropdown, DropdownTrigger, DropdownMenu, DropdownItem } from '@nextui-org/react';
import Link from 'next/link';

// ========== PROFILE DROPDOWN COMPONENT ==========
export const ProfileDropdown: React.FC = () => {
  // Getting the authenticated user
  const { user }: any = useUser();

  // Setting the icon classes
  const iconClasses = 'text-xl text-default-500 pointer-events-none flex-shrink-0';

  return (
    user && (
      <Dropdown>
        <DropdownTrigger>
          <div className="flex items-center">
            <Avatar size="lg" src={user?.picture} style={{ border: '4px solid #8B5CF6' }} />
          </div>
        </DropdownTrigger>
        <DropdownMenu variant="faded" aria-label="Dropdown menu with icons">
          <DropdownItem key="explore" className="text-indigo-700" startContent={<ExploreIcon />}>
            <Link href="#">Explore</Link>
          </DropdownItem>

          <DropdownItem
            key="saved-automations"
            className="text-indigo-700"
            startContent={<SaveIcon />}
          >
            <Link href="#">Saved Automations</Link>
          </DropdownItem>

          <DropdownItem key="profile" className="text-indigo-700" startContent={<ProfileIcon />}>
            <Link href="#">Profile</Link>
          </DropdownItem>

          <DropdownItem key="logout" className="text-danger" startContent={<LogoutIcon />}>
            <Link href="/api/auth/logout">Logout</Link>
          </DropdownItem>
        </DropdownMenu>
      </Dropdown>
    )
  );
};
