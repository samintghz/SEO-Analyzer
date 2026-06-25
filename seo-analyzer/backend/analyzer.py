from collections import Counter
import re
import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin


def analyze_website(url, keyword=None):

    try:

        start_time = time.time()

        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        load_time = time.time() - start_time

        soup = BeautifulSoup(response.text, "html.parser")


        # Title analysis

        title = (
            soup.title.string.strip()
            if soup.title and soup.title.string
            else None
        )


        title_score = 0

        if title:
            if 30 <= len(title) <= 60:
                title_score = 20
            else:
                title_score = 10



        # Meta description analysis

        description = soup.find(
            "meta",
            attrs={"name": "description"}
        )


        description_text = (
            description.get("content")
            if description
            else None
        )


        description_score = 0

        if description_text:
            if 120 <= len(description_text) <= 160:
                description_score = 20
            else:
                description_score = 10



        # Keyword and Word Count Analysis

        page_text = soup.get_text()

        words = re.findall(
            r'\b[a-zA-Z]{3,}\b',
            page_text.lower()
        )


        word_count = len(words)

        unique_words = len(set(words))

        word_frequency = Counter(words)

        top_keywords = word_frequency.most_common(10)


        keyword_analysis = {
            "word_count": word_count,
            "unique_words": unique_words,
            "top_keywords": top_keywords
        }


        if keyword:

            keyword = keyword.lower()

            keyword_analysis["keyword"] = keyword


            keyword_analysis["in_title"] = (
                keyword in title.lower()
                if title
                else False
            )


            keyword_analysis["in_description"] = (
                keyword in description_text.lower()
                if description_text
                else False
            )


            headings_text = " ".join(
                [
                    h.get_text()
                    for h in soup.find_all(
                        ["h1", "h2", "h3"]
                    )
                ]
            ).lower()


            keyword_analysis["in_headings"] = (
                keyword in headings_text
            )



        # Heading analysis

        headings = len(
            soup.find_all(
                ["h1", "h2", "h3"]
            )
        )


        heading_score = 20 if headings > 0 else 0



        # Images ALT analysis

        images = soup.find_all("img")

        image_alt_score = 0


        if images:

            images_with_alt = [
                img for img in images
                if img.get("alt")
            ]


            image_alt_score = int(
                (len(images_with_alt) / len(images)) * 20
            )

        else:

            image_alt_score = 20




        # Broken links analysis

        links = soup.find_all(
            "a",
            href=True
        )


        total_links = len(links)

        broken_links = []


        for link in links[:3]:

            href = link.get("href")

            full_url = urljoin(
                url,
                href
            )


            try:

                link_response = requests.get(
                    full_url,
                    timeout=1,
                    allow_redirects=True,
                    headers={
                        "User-Agent": "Mozilla/5.0"
                    }
                )


                if link_response.status_code >= 400:

                    broken_links.append(
                        {
                            "url": full_url,
                            "status": link_response.status_code
                        }
                    )


            except:

                broken_links.append(
                    {
                        "url": full_url,
                        "status": "unreachable"
                    }
                )



        # Performance score

        performance_score = 20


        if load_time > 3:

            performance_score = 5

        elif load_time > 1.5:

            performance_score = 10



        # Total Score

        total_score = (
            title_score +
            description_score +
            heading_score +
            image_alt_score +
            performance_score
        )



        # Categories

        technical_score = (
            title_score +
            description_score +
            heading_score
        )


        accessibility_score = image_alt_score


        seo_categories = {

            "technical_seo": technical_score,

            "content_seo": heading_score + description_score,

            "performance": performance_score,

            "accessibility": accessibility_score

        }



        # Recommendations

        recommendations = []


        if not title:

            recommendations.append(
                "Add a title tag to improve SEO"
            )


        if not description_text:

            recommendations.append(
                "Add a meta description"
            )


        if headings == 0:

            recommendations.append(
                "Add heading structure (H1, H2, H3)"
            )


        if images and image_alt_score < 20:

            recommendations.append(
                "Add ALT attributes to images"
            )


        if load_time > 3:

            recommendations.append(
                "Improve website loading speed"
            )


        if broken_links:

            recommendations.append(
                f"Fix {len(broken_links)} broken links"
            )



        return {

            "url": url,

            "seo_score": total_score,


            "analysis": {

                "title": title,

                "description": description_text,

                "headings": headings,

                "title_score": title_score,

                "description_score": description_score,

                "heading_score": heading_score,

                "image_alt_score": image_alt_score,

                "performance_score": performance_score,

                "load_time": round(load_time, 2),


                "links_analysis": {

                    "total_links": total_links,

                    "broken_links": len(broken_links)

                },


                "categories": seo_categories,


                "keyword_analysis": keyword_analysis

            },


            "recommendations": recommendations

        }



    except Exception as e:

        return {
            "error": str(e)
        }