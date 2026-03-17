export const BASE_API = 'http://localhost:8000';

interface ReadNote {
	id: number;
	title: string;
	description: string | null;
	create_at: string;
	updated_at: string;
}

export async function getNotes(search?: string): Promise<ReadNote[]> {
	const url = new URL(`${BASE_API}/notes/`);

	if (search) {
		url.searchParams.set('search', search);
	}

	const result = await fetch(url);

	if (!result.ok) {
		throw new Error('Failed to fetch notes!');
	}

	const data: { notes: ReadNote[] } = await result.json();

	return data.notes;
}
