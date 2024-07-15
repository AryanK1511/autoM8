// Or, it's slightly more efficient to use the `req`, `res` args if you're
// using another part of the SDK like `withApiAuthRequired` or `getSession`.
import { NextResponse } from 'next/server';
import { getAccessToken, withApiAuthRequired } from '@auth0/nextjs-auth0';

const GET = withApiAuthRequired(async function GET(req) {
  const res = new NextResponse();
  const { accessToken } = await getAccessToken();
  console.log(accessToken);
  return NextResponse.json({ foo: 'bar' }, res);
});

export { GET };
