import pytest


@pytest.fixture
def currently_reading_response():
    return '''
        <GoodreadsResponse>
           <shelf exclusive="true" id="119211971" name="currently-reading" sortable="false" />
           <reviews start="1" end="2" total="2">
              <review>
                 <id>3479228839</id>
                 <book>
                    <id type="integer">32597955</id>
                    <isbn>8525062502</isbn>
                    <isbn13>9788525062505</isbn13>
                    <text_reviews_count type="integer">59</text_reviews_count>
                    <uri>kca://book/amzn1.gr.book.v1.D7WH6RJ1wgQ3jG50V3gpng</uri>
                    <title>História de Quem Foge e de Quem Fica</title>
                    <title_without_series>História de Quem Foge e de Quem Fica</title_without_series>
                    <image_url>https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1476297694l/32597955._SX98_.jpg</image_url>
                    <small_image_url>https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1476297694l/32597955._SY75_.jpg</small_image_url>
                    <large_image_url />
                    <link>https://www.goodreads.com/book/show/32597955-hist-ria-de-quem-foge-e-de-quem-fica</link>
                    <num_pages>416</num_pages>
                    <format>Paperback</format>
                    <edition_information />
                    <publisher>Biblioteca Azul</publisher>
                    <publication_day>24</publication_day>
                    <publication_year>2016</publication_year>
                    <publication_month>10</publication_month>
                    <average_rating>4.31</average_rating>
                    <ratings_count>84249</ratings_count>
                    <description>No terceiro volume da série napolitana, Lenu e Lila partem para os embates da vida adulta. Numa sequência angustiante e sem espaço para a inocência de outrora, Elena Ferrante coloca o leitor no meio do turbilhão que se forma das amizades, das relações sociais e dos interesses individuais. História de quem foge e de quem fica é uma obra de arte a respeito do amor, da maternidade, da busca por justiça social e de como é transgressor ser mulher em um mundo comandado pelos homens.</description>
                    <authors>
                       <author>
                          <id>44085</id>
                          <name>Elena Ferrante</name>
                          <role />
                          <image_url nophoto="true"><![CDATA[https://s.gr-assets.com/assets/nophoto/user/u_200x266-e183445fd1a1b5cc7075bb1cf7043306.png]]></image_url>
                          <small_image_url nophoto="true"><![CDATA[https://s.gr-assets.com/assets/nophoto/user/u_50x66-632230dc9882b4352d753eedf9396530.png]]></small_image_url>
                          <link><![CDATA[https://www.goodreads.com/author/show/44085.Elena_Ferrante]]></link>
                          <average_rating>4.15</average_rating>
                          <ratings_count>505716</ratings_count>
                          <text_reviews_count>41403</text_reviews_count>
                       </author>
                    </authors>
                    <published>2016</published>
                    <work>
                       <id>26579483</id>
                       <uri>kca://work/amzn1.gr.work.v1.-R0NA0kir1cGxi_fFmUuIQ</uri>
                    </work>
                 </book>
                 <rating>0</rating>
                 <votes>0</votes>
                 <spoiler_flag>false</spoiler_flag>
                 <spoilers_state>none</spoilers_state>
                 <shelves>
                    <shelf exclusive="true" id="119211971" name="currently-reading" review_shelf_id="3117102893" sortable="false" />
                 </shelves>
                 <recommended_for />
                 <recommended_by />
                 <started_at>Tue Aug 04 15:30:16 -0700 2020</started_at>
                 <read_at />
                 <date_added>Tue Aug 04 15:30:16 -0700 2020</date_added>
                 <date_updated>Tue Aug 04 15:30:16 -0700 2020</date_updated>
                 <read_count>1</read_count>
                 <body />
                 <comments_count>0</comments_count>
                 <url><![CDATA[https://www.goodreads.com/review/show/3479228839]]></url>
                 <link><![CDATA[https://www.goodreads.com/review/show/3479228839]]></link>
                 <owned>0</owned>
              </review>
           </reviews>
        </GoodreadsResponse>'''


@pytest.fixture
def currently_reading_list():
   return ['Book 1', 'Book 2']
